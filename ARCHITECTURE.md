# ARCHITECTURE.md

## Directory Responsibilities

```
skills/              ← installable skills; flat — one directory per skill name
docs/                ← knowledge base for this repository
  QUALITY.md         ← acceptance criteria for skills
  WORKFLOW.md        ← authoring and review process
  REFERENCES.md      ← external documentation links
  SECURITY.md        ← security constraints
  specs/             ← per-skill intent; one file per skill (docs/specs/<name>.md)
.github/
  workflows/         ← CI pipeline definitions (GitHub Actions)
scripts/             ← repo-level validators and formatters (Python/uv or Deno only)
.agents/skills/      ← real directory; each skills/<name>/ is symlinked here
                       individually; repo-specific skills may be created here directly
AGENTS.md            ← agent entry point; map only (target 50–100 lines, hard limit 120)
ARCHITECTURE.md      ← this file
```

## Key Invariants

**Skill–spec pairing:** For every directory `skills/<name>/`, a file
`docs/specs/<name>.md` must exist. Names must match exactly. Spec files have no
mandatory section headings or format — their purpose is to clarify the skill's goal
and provide authoring context.

**Flat skills layout:** `skills/` contains only top-level skill directories. No skill
nested inside another skill directory. Each skill directory must contain `SKILL.md`.

**Per-skill symlinks:** `.agents/skills/` is a real directory. Each `skills/<name>/`
has a corresponding symlink `.agents/skills/<name> → ../../skills/<name>`. This allows
repo-specific skills to be created as real directories directly inside `.agents/skills/`
alongside the symlinked entries. Do not replace `.agents/skills/` with a single
directory symlink.

## Skill Directory Structure

Defined by the skills specification (accessible via the `skills-spec` MCP server in
the devcontainer):

```
skills/<name>/
├── SKILL.md          ← required
├── scripts/          ← optional; skill-level scripts (Python/uv or Deno)
├── references/       ← optional; on-demand reference material
└── assets/           ← optional; templates and static resources
```

## Script Language Policy

All scripts in `scripts/` (repo-level) and `skills/<name>/scripts/` (skill-level) must:

- Be Python (uv) or Deno — no other runtimes
- Include a shebang line
- Include inline dependency metadata (`# /// script` block for uv; locked import
  specifiers for Deno)
- Accept all input via CLI flags; no interactive prompts

If a skill bundles scripts, its `SKILL.md` metadata must briefly note the required
runtime (`uv` or `deno`).

## Skill Naming Rules

| Constraint | Rule |
|---|---|
| Characters | Lowercase `a-z`, digits `0-9`, hyphens `-` only |
| Leading/trailing hyphen | Not allowed |
| Consecutive hyphens | Not allowed (`pdf--tools` is invalid) |
| Max length | 64 characters |
| Directory match | `name` in `SKILL.md` frontmatter must equal the parent directory name |

## AGENTS.md Size Budget

Target: 50–100 lines. Hard limit: 150 lines. Exceeding the limit means content should
move to `docs/` with a pointer added to AGENTS.md. Enforced by
`scripts/validate_harness.py` (structural validator).

## Deployment Boundary

`skills/<name>/` is the deployable unit. When a skill is installed in another project,
only the contents of that directory are available — no `docs/`, `scripts/`, `AGENTS.md`,
`WORKFLOW.md`, `QUALITY.md`, or any other file from this repository.

**Consequence for skill authors:** `SKILL.md` body and any skill-local files must be
fully self-contained. Never instruct an agent to read or reference files outside
`skills/<name>/`.

Prohibited in `SKILL.md` body:
- Paths to `docs/`, `scripts/`, or any repo-level file
- References to `docs/specs/<name>.md`, `WORKFLOW.md`, `QUALITY.md`, or `SECURITY.md`
- Instructions to run repo-level scripts (`validate_harness.py`, `check_skill.py`)
