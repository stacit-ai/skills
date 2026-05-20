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

**harness-sync SKILL.md outline:**

```markdown
---
name: harness-sync
description: >
  Create a dedicated consistency skill for a sync concern that lacks one. Use when a
  new consistency need is identified that has no corresponding sync skill, or when a
  reference-based sync rule has grown complex enough to warrant a skill.
---

# Harness Sync (Meta-Skill)

## When to Use
Use when a new consistency concern arises — a new module type, convention, or
integration that requires coordinated updates across files.

## Creating a Specialized Sync Skill
1. Identify the concern: what must stay consistent, and between which files or dirs?
2. Load [assets/project_skill_template.md](../assets/project_skill_template.md)
3. Create `.agents/skills/<concern>-sync/SKILL.md` with:
   - `description`: names the concern and lists trigger paths/conditions
   - Workflow: steps for detecting and correcting drift in that concern
   - Gotchas: non-obvious coupling or ordering requirements
4. Log the new skill in `HARNESS_EVOLUTION.md`

## Naming Patterns

| Concern | Skill name | Description trigger example |
|---|---|---|
| API spec ↔ implementation | `api-spec-sync` | `spec/` or `endpoints/` modified |
| Harness ↔ project structure | `harness-self-sync` | `AGENTS.md` or `.agents/` modified |
| Requirements ↔ tests | `req-test-sync` | `spec/` or `test/` modified |

## Gotchas
- Each skill covers exactly one concern — do not merge concerns into one skill
- Specialized sync skills load automatically; no AGENTS.md entries needed
```

**Document in AGENTS.md governance block:**

```markdown
**Consistency:** when a new consistency concern arises that lacks a dedicated sync
skill, use the `harness-sync` skill to create one.
```
