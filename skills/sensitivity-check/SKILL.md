---
name: sensitivity-check
description: >
  Detects personally identifiable information (PII) and confidential/secret data in
  text or files. Use when scanning for sensitive data, checking for leaked credentials
  or API keys, performing a privacy or compliance review, or verifying content is safe
  to share — even if the user says "find secrets in code", "is there any PII here?",
  "make sure nothing sensitive is included", "check for passwords", "review for
  confidentiality", or "does this contain personal information?".
compatibility: >
  Requires uv and Python 3.11+. Scripts use tiktoken, presidio-analyzer (with spacy),
  and detect-secrets via uv inline dependencies (PEP 723). On non-CUDA systems,
  pii_scan.py requires an extra uv flag; see Step 4a.
---

# Sensitivity Check

## Step 1 — Clarify Scope

Before scanning, confirm:

1. **Target**: Is the input a text string, a single file, or multiple files?
2. **Check type**: PII only / secrets only / both?

If the user has not specified a check type, default to **both**.

## Step 2 — Route Content

Use [`scan_router.py`](scripts/scan_router.py) to classify each item. This must happen before any scan to avoid
consuming the full context window on large files.

```
# For files:
uv run scripts/scan_router.py --files FILE [FILE ...] [--threshold 4000]

# For inline text:
uv run scripts/scan_router.py --text "TEXT" [--threshold 4000]
```

If `uv run` is not available or exits non-zero, `scan_router.py` self-falls-back to a
character-count estimate — use the routing output as-is and note the estimate in the
report.

Each item is classified as one of:

| Method | Condition | Action |
|---|---|---|
| `deep` | ≤ threshold tokens | Read full content directly (Step 3) |
| `script` | > threshold tokens | Run scan scripts (Step 4) |
| `binary` | Non-UTF-8 file | Record path; do not attempt to scan (Step 4d) |

## Step 3 — Deep Check (items routed to `deep`)

Read the full text content. Apply judgment directly without running scripts.

- Load [references/pii_reference.md](references/pii_reference.md) when the check type
  includes PII.
- Load [references/secret_reference.md](references/secret_reference.md) when the check
  type includes secrets.

For each finding: record entity type, location (line number or character offset),
severity level, and a short excerpt. As you read, also apply the false positive
criteria from Step 5.

## Step 4 — Script Check (items routed to `script`)

### 4a. PII scan (when check type includes PII)

**Check CUDA availability before invoking:**

```bash
nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null
```

Use the output to decide how to run [`pii_scan.py`](scripts/pii_scan.py):

| Result | Invocation |
|---|---|
| Exit 0 with output (CUDA present) | `uv run scripts/pii_scan.py --file FILE [FILE ...] [--language en]` |
| Empty output or non-zero exit (no CUDA) | `uv run --extra-index-url https://download.pytorch.org/whl/cpu --with torch scripts/pii_scan.py --file FILE [FILE ...] [--language en]` |

**If `uv run` fails entirely for `pii_scan.py`**, fall back to regex-based detection
using `grep -E` or Python stdlib `re` (no external dependencies). Minimum patterns
to cover:

```
Email:       [a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}
Phone (E.164/US): (\+?1[\s\-.]?)?\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}
IPv4:        \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
Credit card: \b(?:\d[ \-]?){13,16}\b
```

### 4b. Secrets scan (when check type includes secrets)

Use [`secret_scan.py`](scripts/secret_scan.py) to detect potential secrets.

```
# For files:
uv run scripts/secret_scan.py --file FILE [FILE ...]

# For inline text:
uv run scripts/secret_scan.py --text "TEXT"
```

**If `uv run` fails**, fall back to `grep -rE` for common secret patterns:

```
Private key headers:  -----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----
High-entropy assignments: (api[_\-]?key|secret|token|password|credential)\s*=\s*['"][^'"]{16,}['"]
AWS access key IDs:   AKIA[0-9A-Z]{16}
Generic bearer tokens: Bearer\s+[A-Za-z0-9\-._~+/]+=*
```

### 4c. Review script findings for false positives

For every finding returned by the scripts, read the surrounding context — at least
±10 lines or ±200 characters around the flagged location — and apply the false
positive criteria in Step 5 before recording it as confirmed.

### 4d. Binary files

Record each binary file path in the report. Do not attempt to extract or scan
content.

## Step 5 — Evaluate False Positives

Mark a finding as a false positive when context confirms it is not genuine sensitive
data. Common patterns — note these are examples, not an exhaustive whitelist:

- **Example email addresses**: `@example.com`, `@test.com`, `@domain.com`, any
  address inside documentation or comments explicitly labeled as illustrative
- **GitHub / GitLab noreply emails**: `*@users.noreply.github.com`,
  `*@noreply.github.com`
- **Documentation IP addresses**: `192.168.x.x`, `10.x.x.x`, `127.0.0.1`, `0.0.0.0`
  appearing in README or docs as explanatory values
- **Placeholder / template values**: `YOUR_API_KEY`, `<your-token>`, `REPLACE_ME`,
  `xxxxxxxx`, `changeme`, or any value that is clearly a substitution marker
- **Explicit suppression annotations**: the line (or the line immediately above)
  carries a tool suppression comment such as `# pragma: allowlist secret`,
  `# gitleaks:allow`, `# nosec`, or an equivalent directive — treat as intentionally
  allowed and note the annotation in the report

Do not treat these patterns as absolute rules. A `@example.com` address in a real
exported user database is still a genuine finding. Always use judgment.

## Step 6 — Generate Report

Load [assets/report_template.md](assets/report_template.md) and fill in every
section. The **Conclusion** must end with one of:

- **"Contains sensitive information: YES"** — one or more confirmed findings remain
  after false-positive filtering
- **"Contains sensitive information: NO"** — all findings were eliminated as false
  positives, or no findings were produced

## Gotchas

- **Route before scanning** — calling `pii_scan.py` on multiple large files without
  routing first will consume the entire context budget.
- **CUDA check must use `nvidia-smi`, not Python** — `torch.cuda.is_available()`
  cannot run before torch is installed; the shell command works in all environments.
- **`--extra-index-url` and `--with torch` are `uv run` CLI flags** — place them on
  the command line between `uv run` and the script path; do not add them inside the
  `# /// script` dependency block.
- **Keep Click as a direct `pii_scan.py` dependency** — Presidio's import chain uses
  it, but an isolated uv script environment may not install it transitively.
- **detect-secrets requires a file path** — `secret_scan.py` writes inline text to a
  temp file automatically; do not pipe text via stdin.
- **presidio-analyzer defaults to English (`en`)** — pass `--language` explicitly for
  non-English content; missing the right spacy model will silently reduce recall.
- **Token count is in GPT-4 (`cl100k_base`) units** — when tiktoken falls back to
  character estimation, the count is approximate; the routing output flags this with
  `"estimated": true`.
- **Binary detection uses UTF-8 probe** — `scan_router.py` reads the first 8 KB; a
  file that is valid UTF-8 in the first 8 KB but binary further in will be misclassified
  as text. For suspicious files, verify manually.

## References

- Load [references/pii_reference.md](references/pii_reference.md) when the check
  scope includes PII.
- Load [references/secret_reference.md](references/secret_reference.md) when the
  check scope includes secrets or confidential information.
- Load [assets/report_template.md](assets/report_template.md) when generating the
  final scan report.
