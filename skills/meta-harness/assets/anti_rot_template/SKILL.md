---
name: anti-rot
description: >
  Perform a harness sync check after a functional project change. Use when code,
  structure, configuration, or conventions have been modified, when closing a task
  that changed project behavior, when asked to "check harness consistency", "update
  harness after changes", or "make sure harness is up to date".
---

# Anti-Rot (Meta-Skill)

Ensures every functional change is followed by a harness consistency check before the
task closes — preventing the gradual divergence of harness documentation from project
reality.

## Trigger Conditions

Load this skill when any of the following is true:

- A task that modified code, directory structure, configuration, or conventions is
  about to close
- Project behavior has changed (new feature, refactor, renamed module, etc.)
- Asked to "check harness consistency", "update harness after changes", or "make sure
  harness is up to date"

## Produces

- Zero or more updated harness files (depends on what the change set touched)
- Optionally, an entry in `[insert path to evolution log, e.g. HARNESS_EVOLUTION.md]`
  if a substantive update was made

## Workflow

Scan the change set against the sync table. For each matching row, perform the
required update before marking the task complete.

| Change type | Required harness update |
|---|---|
| New directory or package added | Update AGENTS.md directory tree |
| File or API renamed | Update all skills and KB files that reference the old name |
| Convention changed (style, naming, pattern) | Update AGENTS.md conventions + relevant KB file |
| Security rule added or changed | Update QUALITY.md or the designated security file |
| Skill behavior corrected | Add or update a Gotcha in the relevant SKILL.md immediately |
| Harness component removed | Remove all cross-references in AGENTS.md, KB, and other skills |
| New recurring error identified | Add a Hook or Gotcha in the relevant skill |
| Deployed meta-skill content has become stale (path renamed, convention changed) | Update the affected `[insert ...]` values in the corresponding `.agents/skills/<name>/SKILL.md` |

If no row matches, the task is clean — no harness update needed. If a substantive
update was made, log it in `[insert path to evolution log]`.

## Gotchas

- **Auto-discovered** — this skill is loaded by the framework via its `description`
  field; do not add it to AGENTS.md.
- **Skills, hooks, and MCP configs are auto-discovered** — removing them requires no
  AGENTS.md update, but all cross-references in KB and other skills must be removed.
- **"New recurring error identified" means observed in practice**, not anticipated.
  Do not add pre-emptive Gotchas for errors that haven't occurred yet.
