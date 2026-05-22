# Active Governance Reference

Load when setting governance mode to **Active**. Provides the protocols that enable
an agent to autonomously evolve the harness without introducing drift or rot.

---

## Skill Refinement: The 3× Rule

Distill a behavior into a project skill when it has been performed three or more times
with substantially identical instructions across separate task executions.

**Process:**

1. **Detect** — the same multi-step instruction sequence has been regenerated ≥ 3
   times. Minor parameter variation does not reset the count; the logical task must be
   the same.
2. **Confirm scope** — the behavior is self-contained and not better served by updating
   an existing skill.
3. **Distill** — load
   [assets/project_skill_template.md](../assets/project_skill_template.md), create
   `.agents/skills/<name>/SKILL.md` with the procedure.
4. **Log** — add an entry to `HARNESS_EVOLUTION.md`. Load
   [assets/harness_evolution_template.md](../assets/harness_evolution_template.md) if
   the file does not yet exist.

Agent frameworks discover and load skills automatically via their `description` field —
no AGENTS.md update is needed when a new skill is created.

**What counts as a repetition:** same logical task with the same non-obvious steps or
ordering requirements — not minor variations in parameters or inputs.

---

## Anti-Rot Sync Protocol

Every functional change to the project must trigger a harness sync check. At the end
of each task, scan the change set against this table:

| Change type | Required harness update |
|---|---|
| New directory or package added | Update AGENTS.md directory tree |
| File or API renamed | Update all skills and KB files that reference the old name |
| Convention changed (style, naming, pattern) | Update AGENTS.md conventions + relevant KB file |
| Security rule added or changed | Update relevant quality/security documentation (typically QUALITY.md or the designated security file) |
| Skill behavior corrected | Add or update a Gotcha in the relevant SKILL.md immediately |
| Harness component removed | Remove all cross-references in AGENTS.md, KB, and other skills |
| New recurring error identified | Add a Hook or Gotcha in the relevant skill |

If any row matches, perform the harness update before closing the task. A task that
modifies project behavior without updating the harness is incomplete.

---

## Evolution Log Maintenance

For long-term projects, `HARNESS_EVOLUTION.md` records the chronological history of
harness changes. Load [assets/harness_evolution_template.md](../assets/harness_evolution_template.md)
to initialize it if it does not exist.

**When to add an entry:**
- A new skill is created (any reason)
- AGENTS.md is structurally reorganized
- A harness component is removed
- A governance rule is changed
- An anti-rot sync produces a substantive update (not typo fixes)

**Entry cadence:** real-time, not batch. An entry added at the time of the change is
useful. A batch update written weeks later from memory is not.

---

## Governance Documentation

In Active mode, document the following in AGENTS.md (or a dedicated KB file if the
AGENTS.md budget is tight):

```markdown
## Governance

**Mode:** Active
**Skill refinement trigger:** behavior repeated ≥ 3 times across task executions
**Anti-rot:** harness sync check required on every functional change
**Evolution log:** HARNESS_EVOLUTION.md (newest entries first)
```

This block ensures future agents operating on the project inherit the active governance
intent rather than defaulting to passive behavior.

---

## Harness-Sync: Meta-Skill for Consistency

`harness-sync` is a **meta-skill** — its purpose is to create dedicated per-concern
consistency skills, not to enforce consistency directly.

**Create `.agents/skills/harness-sync/` when:**
- The project is Thick (Long-term Maintainable), or
- Active governance mode is enabled, or
- An existing reference-based sync file has grown beyond ~80 lines

**What harness-sync produces:** one dedicated `.agents/skills/<concern>-sync/` skill
per consistency concern. Each specialized skill has a `description` field that loads
automatically on relevant changes:

```markdown
---
name: api-spec-sync
description: >
  Keep API spec aligned with endpoint implementations. Use when spec/, endpoints/, or
  route handler files are modified, or when a new endpoint is added or removed.
---
```

Agent frameworks load specialized sync skills automatically via their descriptions —
no AGENTS.md entry is needed for individual sync skills.

**Template:** load [assets/harness_sync_template/SKILL.md](../assets/harness_sync_template/SKILL.md)
and copy the full `../assets/harness_sync_template/` directory to
`.agents/skills/harness-sync/`. Customize the naming patterns and description trigger
paths to match this project's directory structure.

**Document in AGENTS.md governance block:**

```markdown
**Consistency:** when a new consistency concern arises that lacks a dedicated sync
skill, use the `harness-sync` skill to create one.
```

---

## Active Governance Meta-Skill Set

In Active mode, harness self-evolution should be **framework-driven**, not
memory-dependent. Accomplish this by creating a set of meta-skills in
`.agents/skills/` whose `description` fields cause the framework to auto-load them
at precisely the right moment — when a behavior repeats, when a workflow grows complex,
or when a task changes project behavior.

**Create all four meta-skills when enabling Active governance.** They are
auto-discovered via their `description` fields; no AGENTS.md entry is needed for any
of them.

To create a meta-skill, copy the full template directory to
`.agents/skills/<name>/`, then generate a patch that fills in all `[insert ...]`
markers with project-specific values:

| Meta-skill | Template |
|---|---|
| `skill-refine` | [assets/skill_refine_template/SKILL.md](../assets/skill_refine_template/SKILL.md) |
| `workflow-promote` | [assets/workflow_promote_template/SKILL.md](../assets/workflow_promote_template/SKILL.md) |
| `anti-rot` | [assets/anti_rot_template/SKILL.md](../assets/anti_rot_template/SKILL.md) |
| `harness-sync` | [assets/harness_sync_template/SKILL.md](../assets/harness_sync_template/SKILL.md) |

---

### `skill-refine` — Autonomous Skill Distillation

Handles the 3× rule end-to-end without requiring the agent to recall the rule from
memory. Load [assets/skill_refine_template/SKILL.md](../assets/skill_refine_template/SKILL.md)
and deploy to `.agents/skills/skill-refine/`.

---

### `workflow-promote` — Workflow → Skill Upgrade

Prevents workflow sections from growing unwieldy by upgrading them to skills before
they become hard to maintain. Load
[assets/workflow_promote_template/SKILL.md](../assets/workflow_promote_template/SKILL.md)
and deploy to `.agents/skills/workflow-promote/`.

---

### `anti-rot` — Post-Change Harness Sync

Ensures every functional change is followed by a harness consistency check before the
task closes. Load [assets/anti_rot_template/SKILL.md](../assets/anti_rot_template/SKILL.md)
and deploy to `.agents/skills/anti-rot/`.

---

### Summary Table

| Meta-skill | Auto-load trigger (description) | What it does |
|---|---|---|
| `skill-refine` | Same behavior executed ≥ 3 times | Distills behavior into a new skill |
| `workflow-promote` | Workflow section grows complex | Upgrades workflow section to a skill |
| `anti-rot` | Functional change closes | Runs harness sync check |
| `harness-sync` | New consistency concern arises | Creates a dedicated per-concern sync skill |

All four are auto-discovered by the framework via their `description` fields.
**No AGENTS.md entry is needed for any of them.**

Update the AGENTS.md governance block to reference the meta-skill set:

```markdown
## Governance

**Mode:** Active
**Skill refinement trigger:** behavior repeated ≥ 3 times across task executions
**Anti-rot:** `anti-rot` skill runs after every functional change
**Evolution log:** HARNESS_EVOLUTION.md (newest entries first)
**Consistency:** `harness-sync` skill creates dedicated per-concern sync skills
**Meta-skills:** skill-refine, workflow-promote, anti-rot, harness-sync (auto-loaded)
```
