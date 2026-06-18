# Skills

[![Secret Scanning](https://github.com/stacit-ai/skills/actions/workflows/secret.yml/badge.svg)](https://github.com/stacit-ai/skills/actions/workflows/secret.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Reusable, self-contained **agent skills**: instruction sets that an LLM loads to perform a class
of tasks consistently (authoring, review, validation loops, gotchas, templates).

## Quick Start

1. Pick a skill in `skills/<name>/`.
2. Install it by copying that directory into your agent runtime’s skills folder.
   - **Codex CLI** (example): copy into `$CODEX_HOME/skills/` (or your configured skills path).
3. Trigger it by name in a prompt (or via your runtime’s skill activation UI).

Every skill is a standalone deployable unit: when installed elsewhere, **only**
`skills/<name>/` is available. See `ARCHITECTURE.md` for the deployment boundary rule.

## Included Skills

| Skill | What it does |
|---|---|
| `programming-guidelines` | Universal coding standards (think first, keep it simple, make surgical changes). |
| `git-commit` | End-to-end commit workflow (conventions, atomicity, sensitive data scan, local checks, commit). |
| `conventional-commits` | Draft Conventional Commits 1.0.0 messages (type/scope/body guidance). |
| `gitmoji` | Draft gitmoji-style commit messages (emoji selection + format). |
| `design-md-creator` | Create/maintain a project `DESIGN.md` design system (tokens + prose + validation loop). |
| `meta-harness` | Design and evolve an agent harness (AGENTS.md, skills, KB, tooling, MCP connectivity). |
| `skill-creator` | Create or improve skills (structure, gotchas, references/assets, scripts, review readiness). |
| `sensitivity-check` | Scan text/files for PII and secrets; includes scripts for large inputs. |

## Repository Structure

| Path | Purpose |
|---|---|
| `skills/` | Installable skills (flat layout: one directory per skill). |
| `docs/specs/` | Per-skill intent definitions (paired 1:1 with `skills/<name>/`). |
| `docs/` | Knowledge base: `QUALITY.md`, `WORKFLOW.md`, `REFERENCES.md`, `SECURITY.md`. |
| `scripts/` | Repo-level validators (run before committing skill changes). |
| `.agents/skills/` | Per-skill symlinks for self-application inside this repo. |

## Contributing

Start here:

- Agent entry point: [AGENTS.md](AGENTS.md)
- Authoring process: [docs/WORKFLOW.md](docs/WORKFLOW.md)
- Acceptance criteria: [docs/QUALITY.md](docs/QUALITY.md)
- Security rules (secrets/PII/external content): [docs/SECURITY.md](docs/SECURITY.md)

Validation (run before committing):

```sh
# Repo structure: required files, spec↔skill pairing, per-skill symlinks, AGENTS.md budget
uv run scripts/validate_harness.py

# Skill content: frontmatter + body constraints (run for the skill(s) you changed)
uv run scripts/check_skill.py skills/<name>/
```

## License

Repository license: Apache 2.0 (see `LICENSE`). Individual skills may declare an additional
license in their `SKILL.md` frontmatter.
