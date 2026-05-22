---
name: workflow-promote
description: >
  Upgrade a WORKFLOW.md section to a dedicated project skill. Use when a workflow
  section exceeds ~20 lines, contains branching logic, coordinates changes across
  4 or more files, when the project is transitioning to Active governance or being
  reclassified as Thick, or when asked to "convert workflow to skill", "this workflow
  is getting complex", or "promote this to a skill".
---

# Workflow Promote (Meta-Skill)

Prevents workflow sections from becoming maintenance burdens by promoting them to
structured, auto-loaded skills before they exceed maintainable complexity.

## Trigger Conditions

Load this skill when any of the following is true:

- A `[insert path to WORKFLOW.md, e.g. WORKFLOW.md]` section exceeds ~20 lines
- A workflow step contains branching logic ("if X do Y else Z")
- A workflow coordinates changes across ≥ 4 files
- The project is transitioning to Active governance or being reclassified as Thick
- Asked to "convert workflow to skill", "this workflow is getting complex", or
  "promote this to a skill"

## Produces

- `.agents/skills/<name>/SKILL.md` — the promoted skill
- Modified `[insert path to WORKFLOW.md]` (source section replaced with a one-line
  pointer)
- An entry in `[insert path to evolution log, e.g. HARNESS_EVOLUTION.md]`

## Workflow

1. Identify the section to promote: file path + section heading.
2. Load [assets/workflow_template.md](assets/workflow_template.md), then
   create `.agents/skills/<name>/SKILL.md` with:
   - `description`: trigger conditions derived from the section's When-to-run text
   - Workflow steps migrated and tightened from the source section
   - Gotchas: non-obvious facts extracted from the section
3. Replace the source section in `[insert path to WORKFLOW.md]` with a one-line
   pointer: `- [Concern]: use the '<name>' skill.`
4. If the removed section had a pointer row in AGENTS.md, evaluate whether to keep it
   as entering-agent context or remove it. The skill itself needs no AGENTS.md row.
5. Log the promotion in `[insert path to evolution log]`.

## Gotchas

- **Auto-discovered** — the new skill and this skill are loaded by the framework via
  their `description` fields; do not add either to AGENTS.md.
- **Do not promote a section whose trigger is too broad** — one skill = one coherent
  concern. Split the section if it covers multiple unrelated concerns before promoting.
- **The AGENTS.md pointer row is optional** — it provides context for entering agents
  but is not required for framework loading. Retain it only if it adds value beyond
  what the skill's description already provides.
