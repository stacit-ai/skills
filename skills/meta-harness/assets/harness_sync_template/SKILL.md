---
name: harness-sync
description: >
  Create a dedicated consistency skill for a sync concern that lacks one. Use when a
  new consistency need is identified that has no corresponding sync skill, or when a
  reference-based sync rule has grown complex enough to warrant a skill.
---

# Harness Sync (Meta-Skill)

Creates dedicated per-concern consistency skills rather than enforcing consistency
directly — keeping each sync concern isolated, auto-loadable, and maintainable.

## Trigger Conditions

Load this skill when any of the following is true:

- A new consistency concern arises (a new module type, convention, or integration
  that requires coordinated updates across multiple files) and no dedicated sync
  skill exists for it
- An existing reference-based sync file or section has grown beyond ~80 lines
- A reference-based sync concern is being upgraded to skill-based (Active governance
  mode is being enabled or the project is being reclassified as Thick)

## Produces

- `.agents/skills/<concern>-sync/SKILL.md` — the new per-concern consistency skill
- An entry in `[insert path to evolution log, e.g. HARNESS_EVOLUTION.md]`

## Workflow

1. Identify the concern: what must stay consistent, and between which files or
   directories?
2. Load [assets/skill_template.md](assets/skill_template.md), then
   create `.agents/skills/<concern>-sync/SKILL.md` with:
   - `description`: names the concern and lists the file paths or conditions that
     trigger it (e.g., "Use when `spec/` or `endpoints/` are modified")
   - Workflow: steps for detecting and correcting drift in that concern
   - Gotchas: non-obvious coupling or ordering requirements
3. If the concern was previously managed as a reference-based sync section in
   `[insert path to WORKFLOW.md, e.g. WORKFLOW.md]`, replace that section with a
   one-line pointer to the new skill.
4. Log the new skill in `[insert path to evolution log]`.

## Naming Patterns

_Replace the rows below with this project's actual consistency concerns:_

| Concern | Skill name | Description trigger example |
|---|---|---|
| API spec ↔ implementation *(example)* | `api-spec-sync` | `spec/` or `endpoints/` modified |
| Harness ↔ project structure *(example)* | `harness-self-sync` | `AGENTS.md` or `.agents/` modified |
| Requirements ↔ tests *(example)* | `req-test-sync` | `spec/` or `test/` modified |

## Gotchas

- **Auto-discovered** — the new sync skill and this skill are loaded by the framework
  via their `description` fields; do not add either to AGENTS.md.
- **Each skill covers exactly one concern** — do not merge multiple consistency
  concerns into one skill; use one `<concern>-sync` skill per concern.
- **Description trigger must name specific paths or conditions** — a vague description
  ("use when anything changes") will cause the skill to load too broadly or not at all.
