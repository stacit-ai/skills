---
name: git-commit
description: >
  Executes the full git commit workflow: discovers project conventions, checks change
  atomicity, scans the diff for sensitive data, verifies pre-commit hooks, runs local CI
  checks, validates the commit message against the 50/72 rule, and commits. Use when
  creating a git commit, saving changes to version control, or when asked to "commit",
  "checkpoint", "stage and commit", "save my code to git", or "create a commit message".
compatibility: >
  validate_commit_msg.py requires uv and Python 3.11+. The script uses no third-party
  packages.
---

# Git Commit

## Step 1 — Discover Project Conventions

Convention sources are checked in strict priority order. Any aspect **explicitly stated**
in a documentation file is authoritative — do not override it with history or inference.

### 1a. AGENTS.md (highest priority)

Read `AGENTS.md`. Look for a commit conventions section.

- If explicit commit rules are present, record them as **authoritative** for every
  aspect they cover (format, type list, scope requirements, footer fields, etc.).
- If `AGENTS.md` references another file for commit conventions (e.g., "see
  CONTRIBUTING.md for commit format"), follow that pointer and treat the referenced
  file as authoritative instead.

### 1b. CONTRIBUTING.md

If `AGENTS.md` has no commit conventions and no pointer, read `CONTRIBUTING.md`.
Apply the same rule: explicitly stated aspects are authoritative.

### 1c. README.md

If `CONTRIBUTING.md` is absent or has no commit section, scan `README.md` for a
commit or development contributing section.

### 1d. File-tree exploration (fallback)

If none of the above contain explicit commit rules, inspect the repository:

```bash
git ls-files | head -80
```

Identify files that may encode commit conventions (e.g., `.commitlintrc*`,
`commitlint.config.*`, `.gitmessage`, `package.json` → `commitlint` key). Read the
relevant ones. Rules derived this way are **inferred**, not authoritative — they can
be supplemented by history in Step 2.

### Priority table

| Source | Authoritative? | History can fill gaps? |
|---|---|---|
| AGENTS.md (explicit) | Yes | No |
| CONTRIBUTING.md (explicit) | Yes | No |
| README.md (explicit) | Yes | No |
| Config files / git history (inferred) | No | Yes |

Note whether each convention aspect was found explicitly or inferred — this affects
Step 2 and the post-commit suggestion in Step 9.

## Step 2 — Inspect Commit History

**Skip dimensions that Step 1 resolved explicitly.** History only fills gaps.

```bash
git log --oneline -20
```

For each dimension **not** covered by authoritative documentation in Step 1, observe:

- **Type casing** — `feat` vs `Feat` vs `FEAT`
- **Scope usage** — always / never / conditional; separator style `(scope)` vs `[scope]`
- **Footer conventions** — `Closes #N`, `Co-authored-by:`, etc.
- **Scope granularity** — module-level (`auth`) vs file-level (`auth/login.ts`)

History is authoritative for the dimensions it covers, but only for those dimensions.

## Step 3 — Check Change Atomicity

```bash
git diff --cached --stat
git diff --cached
```

A commit is atomic when it makes one logical change to one concern. Split when:

- The diff spans unrelated modules (e.g., `src/auth/` and `docs/`)
- The diff mixes feature code with unrelated test changes
- Multiple unrelated bug fixes appear together
- Refactoring is mixed with functional changes

**If the change set should be split and the user has not explicitly requested a
combined commit:**

1. Present the proposed split with a rationale for each group
2. Confirm with the user before proceeding
3. Create an isolated worktree per commit:
   ```bash
   git worktree add ../commit-<N> HEAD
   ```
4. In each worktree, stage only the relevant files and commit
5. Remove the worktrees when done: `git worktree remove ../commit-<N>`

## Step 4 — Scan for Sensitive Information

Run against the staged diff:

```bash
git diff --cached
```

Check the output for:

- Private keys: `-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----`
- API key assignments: `(api[_-]?key|secret|token|password|credential)\s*[=:]\s*['"][^'"]{16,}['"]`
- AWS Access Key IDs: `AKIA[0-9A-Z]{16}`
- Email addresses that are not clearly placeholder (e.g., not `@example.com`,
  `@users.noreply.github.com`, or labeled as illustrative in context)

If a sensitive-info-guard skill is also loaded, delegate the diff text to it for a
thorough scan.

**On any confirmed finding without explicit user clearance: stop and ask the user to
review before proceeding. Never commit sensitive data silently.**

## Step 5 — Verify Pre-commit Hooks

Determine which hook manager is in use (check in order):

| File/Directory | Manager | Install command |
|---|---|---|
| `.pre-commit-config.yaml` | pre-commit | `pre-commit install --install-hooks` |
| `.husky/` directory | husky | check `.husky/pre-commit` is executable |
| `lefthook.yml` or `lefthook.yaml` | lefthook | `lefthook install` |
| `.git/hooks/pre-commit` | raw hook | check it is executable |

If hooks exist but are not installed, install them before committing.

**Never use `--no-verify` to bypass hooks unless the user explicitly instructs it.**
If a hook fails, read its output and fix the underlying issue.

## Step 6 — Run Local CI Checks

Detect which checks apply and run them. Common examples:

```bash
# JavaScript / TypeScript
npm run lint && npm run typecheck && npm test

# Python
uv run ruff check . && uv run mypy . && uv run pytest

# Go
go vet ./... && go test ./...

# Generic
make check
```

Determine what to run by inspecting `package.json` scripts, `Makefile`, `pyproject.toml`,
or the project's CI config. Run only checks that exist. Stop and report if any check
fails — do not proceed to commit a failing diff.

## Step 7 — Draft Commit Message

Apply the **50/72 rule**:

- **Title**: ≤ 50 characters, imperative mood, lowercase first letter, no trailing period
- **Blank line** between title and body (when a body is present)
- **Body**: each line ≤ 72 characters

**What to write:**

- *Title*: what the change does — imperative sentence ("add rate limiting", not "added
  rate limiting")
- *Body* (if needed): **why** the change was made, what problem it solves, notable
  trade-offs, side effects, or limitations. Do not describe *how* — the diff shows that.

**Short format** (title only): default. Use when the title alone captures intent and
reason — typical for small bug fixes, dependency bumps, single-file changes.

**Long format** (title + body): use when the reason is non-obvious, there are
trade-offs worth documenting, or the user asks for a body.

## Step 8 — Validate Message

Use [`scripts/validate_commit_msg.py`](scripts/validate_commit_msg.py) to check the
message against the 50/72 rule and style conventions before committing:

```bash
uv run scripts/validate_commit_msg.py --message "YOUR TITLE

YOUR BODY LINE 1
YOUR BODY LINE 2"
```

For multi-line messages, write to a file first:

```bash
uv run scripts/validate_commit_msg.py --file /path/to/COMMIT_EDITMSG
```

Fix all reported violations before committing.

## Step 9 — Commit

```bash
# Single-line message
git commit -m "title"

# Multi-line message
git commit -m "title" -m "body paragraph 1" -m "body paragraph 2"

# From a file
git commit -F /path/to/COMMIT_EDITMSG
```

Do not use `--no-verify` unless the user has explicitly instructed it.

**If Step 1 found no explicit commit documentation** (rules were inferred from config
files or history only), suggest to the user after the commit succeeds:

> No commit convention file was found. Consider documenting commit guidelines in
> `AGENTS.md` or `CONTRIBUTING.md` so all contributors and agents apply the same
> format consistently.

## Gotchas

- **Explicit docs win over everything** — a rule stated in `AGENTS.md` or
  `CONTRIBUTING.md` is final; do not second-guess it with history or inference.
- **History fills gaps, not overrides** — if history shows `Fix:` (capitalized) and
  no documentation addresses casing, match history. If documentation states lowercase,
  use lowercase regardless of what history shows.
- **Worktree must not be inside the repo root** — `git worktree add ../commit-N HEAD`
  is safe; placing it inside the repo root can nest the worktree and corrupt staging.
- **`git diff --cached` is empty when nothing is staged** — run `git status` first to
  confirm staging state before diagnosing an empty diff.
- **Pre-commit hooks may reject a valid message format** — if the hook fails on the
  message, read its stderr; a commitlint rule may require a specific type prefix.
  Fix the message; do not bypass with `--no-verify`.
- **50/72 counts Unicode codepoints, not bytes** — a CJK character is one character;
  an emoji is typically one or two codepoints. The validator uses `len()` in Python,
  which counts codepoints.
- **Scope separator varies by project** — `(scope)` is Conventional Commits style;
  `[scope]` and bare `scope/` appear in other conventions. Match what history uses.
