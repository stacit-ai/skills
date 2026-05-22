---
name: meta-harness
description: >
  Design, build, improve, audit, and evolve a project's harness framework — the full
  set of agent-guidance artifacts beyond the model: AGENTS.md, skills, knowledge base,
  quality tooling, hooks, and connectivity (MCP). Use when asked to set up agent
  instructions or a harness, create or update AGENTS.md, improve a project's agent
  setup, add a project-specific skill, build or evolve a harness framework, or when
  the user says "how should agents work in this project", "help me structure the agent
  context", "set up Copilot for this codebase", "the agent doesn't know our
  conventions", "make agents smarter here", or "audit the harness".
---

# Meta-Harness

**Harness** = everything in an agent system except the model: AGENTS.md, skills,
knowledge base, quality tooling, hooks, connectivity (MCP). Core trade-off: constrain
output diversity to gain quality and predictability.

## Persona & Philosophy

Operate as a **Senior Architect**; treat the user as **Product Manager**.

Three invariants — never violate:

1. **Agent-first**: harness files are written for agents, not humans. Plain text,
   directive, no pleasantries, no redundant tokens.
2. **Version-controlled existence**: any instruction not in a committed file or
   registered tool is invisible to future agents. If it matters, it must be committed.
3. **Lean Architecture**: only create a harness component when it serves an immediate,
   concrete need. "Might be useful later" is not sufficient justification.

## Workflow

### 1. Scan the Project

Read: directory structure, existing harness files (AGENTS.md, `.agents/`), tech stack
indicators (package manifests, CI config), README, commit history if available. Infer
project lifecycle phase, team size signals, tech stack, and existing harness health.

Ask only when two valid paths exist and the cost of choosing wrong is high.

### 2. Classify Project Type

Map findings to the Intensity Matrix. A project showing signals of both Long-term and
Exploratory should be treated as Maintainable Exploratory (Medium).

### 3. Assess Current Harness Health

Audit existing harness for:

- **Missing components**: required by the classified thickness but absent
- **Outdated content**: references behavior or structure that no longer exists
- **Budget violations**: AGENTS.md exceeds 150 lines
- **Orphaned references**: pointers to files that don't exist
- **Excess components**: present but not warranted by project type — candidates for
  removal

### 4. Draft Harness Plan

Produce a structured action list: component to add/update/remove, execution order,
governance mode to adopt. Include one-line rationale per action.

Default execution order: AGENTS.md → Skills → Knowledge Base → Quality Tools →
Hooks → MCP.

### 5. Confirm Before High-Risk Actions

Always confirm with the user before:

- Adding any MCP or external connectivity component (security invariant — no exceptions)
- Removing existing harness components
- Making structural changes affecting more than three files

Autonomous execution is appropriate for: creating new skills, adding KB entries,
updating AGENTS.md within budget, establishing governance documentation.

### 6. Execute

Create or update files per the plan. Load asset templates when creating new files:

- Creating or restructuring AGENTS.md → load
  [assets/agents_md_template.md](assets/agents_md_template.md)
- Creating HARNESS_EVOLUTION.md → load
  [assets/harness_evolution_template.md](assets/harness_evolution_template.md)
- Distilling a repeated behavior into a skill → load
  [assets/project_skill_template.md](assets/project_skill_template.md)
- Creating a knowledge base document → load
  [assets/knowledge_entry_template.md](assets/knowledge_entry_template.md)
- Enabling Active governance (creating meta-skills) → for each meta-skill, load the
  corresponding template directory, copy directory to
  `.agents/skills/<name>`, then generate a patch that replaces all
  `[insert ...]` markers and adapts the skill content to fit this project:
  - `skill-refine`: [assets/skill_refine_template](assets/skill_refine_template)
  - `workflow-promote`: [assets/workflow_promote_template](assets/workflow_promote_template)
  - `anti-rot`: [assets/anti_rot_template](assets/anti_rot_template)
  - `harness-sync`: [assets/harness_sync_template](assets/harness_sync_template)

### 7. Verify

After execution:

- Count AGENTS.md lines: must be ≤ 150 (target ≤ 100)
- Confirm AGENTS.md informs agents about harness architecture files (folder pointers
  suffice for multi-file domains; listing every individual file is not required)
- Confirm all internal harness cross-references resolve
- Confirm governance mode is documented in AGENTS.md or a KB file
- Confirm a consistency layer appropriate to the project type is in place
- If Active governance: confirm HARNESS_EVOLUTION.md exists (long-term projects only)

---

## Harness Intensity Matrix

| Project Type | Thickness | Key Components | Consistency Layer | Priority |
|---|---|---|---|---|
| Long-term Maintainable | **Thick** | Full suite: CI/CD, thick KB, fine-grained Skills, Hooks, Linter | Skill-based | Maximum robustness & anti-rot |
| Maintainable Exploratory | **Medium** | Linter, basic KB, Skills for key workflows | Reference-based | Quality ↔ flexibility balance |
| Defined One-off | **Medium** | Detailed architecture/goal doc (DESIGN.md or KB entry) | Inline | Result-focused; skip governance overhead |
| Undefined Exploratory | **Light** | Connectivity (MCP), minimal Linter | Inline or none | Resource access only; maximize autonomy |

---

## Component Quick Reference

### Root-level Convention Files

These live at the project root (not inside `.agents/`):

- **`AGENTS.md`** — harness entry point; must list every other harness file so agents
  know to look for them; budget ≤ 100 lines target, ≤ 150 hard limit
- **`ARCHITECTURE.md`** — technical architecture: directory ownership, module
  boundaries, build/deploy topology; create when requested or when AGENTS.md structural content would exceed the line budget (move
  the overflow here); load when making structural or cross-cutting changes
- **`DESIGN.md`** — frontend visual spec following the
  [Stitch design-md format](https://stitch.withgoogle.com/docs/design-md/overview.md);
  create only for projects with a visual/UI component

Load [assets/agents_md_template.md](assets/agents_md_template.md) when creating or
fully restructuring AGENTS.md.

### Skills (SOPs)

- Location: `.agents/skills/<name>/` — every project-specific skill, no exceptions
- Trigger to create: a workflow is repeatable and benefits from constraint or guidance;
  or the 3× rule has fired (Active mode)
- Auto-discovered: agent frameworks load skills automatically via their `description`
  field — do not list individual skills in AGENTS.md or any other harness document;
  the framework discovers them without explicit registration
- `WORKFLOW.md` or `workflow/` is a lighter alternative when full skill structure is
  not warranted: plain SOP text, referenced from AGENTS.md with file + section heading
  (e.g., 'see WORKFLOW.md §Deploy Process' or 'search for `## Deploy Process` in WORKFLOW.md')
- Load [references/thick_harness_components.md](references/thick_harness_components.md)
  when building skills for a Thick project (detailed structure specs)

### Knowledge Base

Default location: `.agents/knowledge/` — but scan for existing `docs/`, `ADR/`, or
similar first; consolidate rather than split. KB can contain:

| File / Folder | Purpose | Single-file vs folder |
|---|---|---|
| `REFERENCES.md` / `references/` | External doc URLs (prefer llms.txt links) or copied llms.txt files; can also be exposed via MCP | Single file for a short URL list; folder when storing multiple copied docs |
| `PLAN.md` / `plan/` | Current project plans; if using an external PM tool (Linear, etc.) via MCP, keep a `PLAN.md` that explains how MCP manages plans | Single file unless plan has multiple active streams |
| `WORKFLOW.md` / `workflow/` | Operation SOPs; lightweight skill alternative for passive-mode projects | Single file when one process; folder when multiple distinct workflows |
| `SPEC.md` / `spec/` | Project requirements | Single file for contained scope; folder for multi-domain specs |
| `QUALITY.md` | Code quality and security requirements | Always single file |

Single-file vs folder rule: start with a single file; split to a folder when the file
exceeds ~150 lines or contains clearly separable sub-topics.

These are common file types — include only those the project needs, and add others as
appropriate. Not every project requires all five.

Load [assets/knowledge_entry_template.md](assets/knowledge_entry_template.md) when
creating a new KB document.

### Quality Tools

- Apply to both production code and harness files (AGENTS.md budget, skill validity)
- Minimum for Medium/Thick: one linter for the primary language, committed config
- Load [references/thick_harness_components.md](references/thick_harness_components.md)
  for harness-specific quality check requirements (Thick projects)

### Hooks

- Runtime callbacks for correcting specific, documented recurring error patterns
- Determine hook mechanism from the agent framework in use; omit if unsupported
- Auto-loaded: hooks are activated by the framework based on their placement in
  framework-specific locations (e.g., `.cursor/rules/`, `.github/copilot-instructions.md`,
  `CLAUDE.md`) — do not list hooks in AGENTS.md; the framework loads them automatically
  for all relevant operations without registration
- Load [references/thick_harness_components.md](references/thick_harness_components.md)
  for hook placement rules by framework

### Connectivity (MCP)

- Principle: grant only the tools/resources required for declared tasks — no speculative
  access, no capability creep
- **Mandatory confirmation**: always confirm with user before creating any MCP config
- Auto-loaded: MCP servers are loaded from framework-specific config files
  (e.g., `.mcp.json`, `mcp_servers.json`) — do not list MCP servers in AGENTS.md;
  the framework discovers them from config without explicit harness registration
- Mandatory confirmation: always confirm with user before creating any MCP config
- Load [references/connectivity_mcp_security.md](references/connectivity_mcp_security.md)
  before writing any connectivity component

---

## Governance Modes

Select based on harness thickness and project duration:

| Thickness | Duration | Mode |
|---|---|---|
| Thick | Any | Active |
| Medium | Long-running | Active |
| Medium | One-off | Passive |
| Light | Any | Passive |

**Passive mode**: maintain existing harness consistency only. No autonomous component
creation. Flag stale content to the user; do not auto-modify.

**Active mode**: agent autonomously refines harness. When enabling Active mode, follow [references/active_governance.md](references/active_governance.md) to create a self-maintaining harness engineering architectural layer.

Document the selected mode and its triggers in AGENTS.md or a KB file. An undocumented
governance mode is the same as no governance mode.

---

## Consistency Layer

Every harness must include a mechanism for keeping it in sync with the project as
implementation evolves. This applies in both Passive and Active modes — the form
scales with complexity, the requirement does not.

**Inline** (Light, Defined One-off):

When the sync table fits within ~10 lines of AGENTS.md budget, embed it directly:

```markdown
## Keep in Sync

| When this changes | Update this |
|---|---|
| Directory structure | AGENTS.md §Structure |
| API or interface renamed | Relevant skill Gotchas and KB files |
| Convention changed | AGENTS.md §Core Conventions + relevant KB file |
```

When sync rules would overflow the AGENTS.md budget, move the rules to a dedicated
workflow file and leave context-specific pointer lines in AGENTS.md instead:

```markdown
- When adding a new API endpoint, see WORKFLOW.md §API Conventions
- When changing auth rules, search for `# Auth` in docs/security.md
```

**Reference-based** (Maintainable Exploratory — multiple sync concerns, more structure
than inline can provide):

For each sync concern, create a dedicated workflow section or file (single `WORKFLOW.md`
with one section per concern, or a `workflow/` folder when content is too long). In
AGENTS.md, keep one pointer line per concern:

```markdown
- When adding a new API endpoint, see WORKFLOW.md §API Conventions
- When renaming a module, search for `## Module Rename` in WORKFLOW.md
- When auth rules change, see workflow/security-sync.md §Auth Rule Change
```

Load [references/sync_layer.md](references/sync_layer.md) when setting up this form.

**Skill-based** (Long-term Maintainable, or Active mode):

Create **one dedicated skill per sync concern** — not one monolithic sync skill. Each
skill description triggers on relevant file or directory changes, for example:

> "Keep API spec aligned with endpoint implementations. Use when `spec/`, `endpoints/`,
> or related files are modified."

Agents load specialized sync skills automatically via their descriptions — no AGENTS.md
entry is needed. Use the **`harness-sync`** skill (a meta-skill that creates these
specialized skills) when a new consistency concern arises.

Load [references/active_governance.md](references/active_governance.md) for the
harness-sync meta-skill creation procedure.

---

## Security Invariants

- **Never add MCP or external connectivity without explicit user authorization** — this
  applies equally in Active and Passive modes. Adding MCP expands agent capability
  boundaries and may break security guardrails; always present the user confirmation
  template and obtain explicit approval before proceeding.
- Apply the minimal capability principle: grant only the specific tools/resources the
  agent needs for declared tasks. No speculative access.
- Load [references/connectivity_mcp_security.md](references/connectivity_mcp_security.md)
  before writing any MCP configuration — required regardless of governance mode.
- Never embed credentials, API keys, or access tokens in harness files. Use environment
  variable references.

---

## Gotchas

- **Outdated harness is more damaging than no harness** — stale instructions actively
  mislead agents. Every functional change must update the corresponding harness files
  in the same commit. No exceptions.

- **AGENTS.md budget is a hard constraint** — count lines before and after every edit.
  At 150 lines the file must be refactored: move content to KB or referenced docs, not
  compressed or summarized inline.

- **Never create empty subdirectories** — preemptive `.agents/skills/`, `knowledge/`
  directories mislead agents into expecting files that don't exist. Create directories
  only when populating them in the same action.

- **MCP requires explicit user confirmation** — security invariant, not a preference.
  Execute only after confirmation; document the confirmation reference.

- **Skills belong in `.agents/skills/<name>/`** — never in project root, `docs/`, or
  ad-hoc locations. Projects using other conventions should migrate, not accommodate.

- **Knowledge base defaults to `.agents/knowledge/`** — always scan for an existing
  docs convention before choosing a location. Consolidate rather than split.

- **Governance mode must be in the harness** — if not recorded, future agents default
  to passive regardless of intent. Document the mode and its triggers explicitly.

- **HARNESS_EVOLUTION.md is for long-term projects only** — omit for Defined One-off
  and Undefined Exploratory. Its absence is the correct state for those types.

- **Lean Architecture is non-negotiable** — "we might need this later" does not justify
  creating a harness component. Absence of a component is a deliberate choice, not a gap.

- **Monorepo harness is layered** — a root AGENTS.md handles global context; each
  sub-package may have its own `.agents/` directory scoped to that package. Root
  AGENTS.md references sub-harnesses but never duplicates their content.

- **Removing a component requires removing all references to it** — orphaned pointers
  in AGENTS.md or other harness files cause agents to attempt loading non-existent files.
  Clean up all cross-references on removal.

- **AGENTS.md must inform agents about harness architecture layer files** — components
  not discoverable from AGENTS.md are invisible to entering agents. A folder pointer
  (e.g., `spec/` → "when implementing features") is sufficient when a domain has many
  files; listing every individual file is not required and may bloat the budget.

- **Consistency layer is mandatory in all modes** — the form scales (Inline → Reference
  → per-concern Skills), but the requirement does not. In skill-based form, each sync
  concern gets its own dedicated skill loaded automatically by the agent framework. A
  harness without a sync mechanism will drift from the implementation it describes.
