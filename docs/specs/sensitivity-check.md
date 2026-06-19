# Spec: sensitivity-check

## Purpose

Guides an agent through detecting personally identifiable information (PII) and/or
confidential/secret information in text or files. The skill selects a check strategy
based on content size (GPT-4 token count), bundles scripts for automated scanning,
guides false-positive review via context inspection, and produces a structured
conclusion report.

## Trigger Conditions

**Explicit:**
- "check for sensitive information"
- "scan for PII"
- "detect secrets in this file"
- "find leaked credentials"
- "privacy review"
- "audit for sensitive data"
- "check if this file contains personal information"
- "look for API keys or passwords"

**Indirect (must also trigger):**
- "make sure nothing sensitive is included"
- "is there any private data in this?"
- "check before publishing"
- "review for confidentiality"
- "redact sensitive content"
- "this might have passwords or PII"
- "verify this is safe to share"
- "does this contain any secrets?"

## External Dependencies

| Library | Version | Purpose |
|---|---|---|
| `tiktoken` | `>=0.7,<1` | GPT-4 token counting for routing decisions |
| `click` | `>=8,<9` | CLI runtime dependency required by the PII analyzer import chain |
| `presidio-analyzer` | `>=2.2,<3` | PII entity detection via NLP pattern matching |
| `spacy` | `>=3.7,<4` | NLP backend for presidio-analyzer |
| `detect-secrets` | `>=1.4,<2` | Secret/credential pattern detection |

**CUDA-conditional dependency:**
On systems without CUDA, `torch` (CPU-only wheel) must be explicitly provided when
running `pii_scan.py`:
```
uv run --extra-index-url https://download.pytorch.org/whl/cpu --with torch scripts/pii_scan.py ...
```
CUDA availability is detected via `nvidia-smi`; see SKILL.md for the full invocation
decision tree.

## Scope

Covers: inline text strings, single files, batches of files (any mix). Binary files
are recorded but not analyzed. Output is a structured scan report with an explicit
YES/NO conclusion.

**Out of scope:**
- Automated redaction or file modification
- Real-time monitoring or CI pipeline integration
- Scanning password-protected or encrypted archives
- Languages other than English (presidio-analyzer defaults to `en`; multilingual
  content requires explicit `--language` and appropriate spacy models)

## Notes

- All three scripts use `uv run` and declare inline dependencies via PEP 723.
- The CUDA check uses `nvidia-smi` (shell command) rather than
  `torch.cuda.is_available()` because torch may not yet be installed at check time.
- `--extra-index-url` and `--with torch` are `uv run` command-line flags, not fields
  inside the `# /// script` PEP 723 metadata block.
