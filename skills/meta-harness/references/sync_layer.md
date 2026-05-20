# Reference-based Consistency Layer

Load when setting up a **reference-based consistency layer** for a medium-complexity
project (Maintainable Exploratory). Describes how to create workflow files per sync
concern and connect them to AGENTS.md.

---

## When to Use Reference-based (vs Inline vs Skill-based)

**Choose Inline** when the full sync mapping fits in ~10 lines inside AGENTS.md
without exceeding the budget — typically Light projects or simple one-off repos with
fewer than five distinct harness files.

**Choose Reference-based** when:
- There are multiple distinct sync concerns, each needing step-by-step procedures
- The total sync content would exceed the AGENTS.md budget if kept inline
- The project is Maintainable Exploratory

**Upgrade to Skill-based** when:
- A workflow section exceeds ~20 lines or contains branching logic
- A workflow coordinates changes across ≥ 4 files
- The project transitions to Active governance or is reclassified as Thick

---

## Sync Workflow File Structure

Create one workflow section per sync concern. Default: a single `WORKFLOW.md` (or
place inside an existing `workflow/` folder) with one section per concern. Split into
a folder when the file exceeds ~150 lines or concerns are cleanly separable.

```markdown
## [Sync Concern 1: e.g., New API Endpoint]

Run this workflow when adding a new API endpoint.

1. [Step: open the relevant file and navigate to the correct section]
2. [Step: what to add, change, or verify]
3. [Step: how to confirm the update is correct]

## [Sync Concern 2: e.g., Module Rename]

Run this workflow when renaming a module or top-level directory.

1. ...
```

**Common sync concerns for most projects:**

| Concern | When to run |
|---|---|
| New API endpoint | New route or handler added |
| Module / directory rename | Module renamed or moved |
| Convention change | Naming or style convention updated |
| Auth rule change | Auth requirements added or changed |
| Harness update | AGENTS.md or `.agents/` content modified |

Include only the concerns that apply — omit others.

---

## Connecting to AGENTS.md

Add one pointer line per concern to AGENTS.md. Context-specific pointers ensure agents
read only what is relevant to their current task:

```markdown
- When adding a new API endpoint, see WORKFLOW.md §New API Endpoint
- When renaming a module, search for `## Module Rename` in WORKFLOW.md
- When auth rules change, see workflow/security-sync.md §Auth Rule Change
```

Do not use a single generic row ("see X when making any changes") — specific pointers
are more actionable and prevent agents from reading irrelevant content.

Skills created via the upgrade path (see Upgrade Checklist below) do not need
AGENTS.md entries — agent frameworks load them automatically via their `description`
field.

---

## Writing Effective Workflow Steps

Each step must be specific enough to execute without interpretation:

- **Good**: "Open AGENTS.md, search for the `## Structure` heading, add one line
  `├── <new-dir>/  ← <one-line description>` to the tree"
- **Bad**: "Update AGENTS.md" — too vague; agent cannot act without re-reading everything

When a step requires branching logic or coordinates changes across ≥ 4 files, consider
upgrading that concern to a skill.

---

## Upgrade Checklist: Reference → Skill

Consider upgrading to skill-based when any of these is true:

- [ ] A workflow section exceeds ~20 lines
- [ ] Any workflow step requires branching conditions or "if X do Y else Z" logic
- [ ] A workflow coordinates changes across ≥ 4 files
- [ ] The project is being reclassified from Medium to Thick
- [ ] Active governance mode is being enabled

To upgrade: load
[`../references/active_governance.md`](active_governance.md) and follow the
Harness-Sync section. The upgrade creates one dedicated `.agents/skills/<concern>-sync/`
skill per domain using the `harness-sync` meta-skill; no AGENTS.md entries are needed
for the resulting skills.
