---
name: skill-refine
description: >
  Distill a repeated behavior into a new project skill following the 3× rule. Use when
  the same multi-step instruction sequence has been executed 3 or more times across
  separate tasks, when a recurring workflow lacks a dedicated skill, when asked to
  "create a skill for X", "we keep doing this the same way", or "make this into a
  skill".
---

# Skill Refine (Meta-Skill)

Converts a behavior that has been manually repeated ≥ 3 times into a versioned,
auto-loaded project skill — eliminating the need to reconstruct instructions from
scratch on every recurrence.

## Trigger Conditions

Load this skill when any of the following is true:

- The same multi-step instruction sequence has been executed in ≥ 3 separate task
  sessions (not ≥ 3 calls within one task)
- A recurring workflow exists but has no dedicated skill in `.agents/skills/`
- Asked to "create a skill for X", "we keep doing this the same way", or "make this
  into a skill"

## Produces

- `.agents/skills/<name>/SKILL.md` — the new project skill
- An entry in `[insert path to evolution log, e.g. HARNESS_EVOLUTION.md]`

## Workflow

1. Confirm the behavior has been performed ≥ 3 times with substantially identical
   steps. Minor input variation does not reset the count; the logical task must be
   the same.
2. Confirm scope: the behavior is self-contained and not better served by updating
   an existing skill.
3. Load [assets/skill_template.md](assets/skill_template.md), then
   create `.agents/skills/<name>/SKILL.md` with the distilled procedure.
4. Log the new skill in `[insert path to evolution log]` (create it from the harness
   evolution template if it does not yet exist).

## Gotchas

- **Auto-discovered** — the new skill and this skill are both loaded by the framework
  via their `description` fields; do not add either to AGENTS.md.
- **Count task executions, not calls within one task** — three separate sessions, not
  three loops inside one session. A single long task that repeats the same steps
  internally counts as one execution, not three.
