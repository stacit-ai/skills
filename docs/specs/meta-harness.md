# Spec: meta-harness

## Purpose

Guides an agent to act as a Senior Architect when designing, building, improving,
auditing, and evolving a project's harness — the full set of agent-guidance artifacts
beyond the model itself: AGENTS.md, skills, knowledge base, quality tooling, hooks,
and connectivity (MCP).

The skill serves both roles:

1. **Context provision** — supplies the Harness Intensity Matrix, component library
   specifications, governance protocols, and anti-rot mechanisms the agent cannot
   reliably produce from training knowledge alone.
2. **Output restriction** — constrains agent behavior via the Architect persona, a
   structured workflow, and explicit security invariants, reducing variance in harness
   quality across projects.

## Trigger Conditions

**Explicit:**
- "set up a harness for this project"
- "create an AGENTS.md"
- "improve the agent harness"
- "audit the harness"
- "add a skill to this project"
- "evolve the harness"
- "build the agent setup"
- "manage the project harness"
- "update AGENTS.md"

**Indirect (must also trigger):**
- "how should agents work in this project"
- "help me structure the agent context"
- "set up Copilot/agent for this codebase"
- "make agents smarter here"
- "improve agent quality"
- "the agent keeps making the same mistakes"
- "how do I teach the agent about this project"
- "what harness components does this project need"
- "help me decide between active and passive governance"
- "the agent doesn't know our conventions"

## What the Agent Lacks

Without this skill, an agent would likely:

- Apply a one-size-fits-all harness instead of calibrating depth to project type
- Create all harness components preemptively (AGENTS.md + Skills + KB + Hooks + MCP)
  even when most are unnecessary, violating the lean architecture principle
- Exceed the AGENTS.md line budget by embedding detailed instructions inline rather
  than using progressive disclosure with pointers to referenced documents
- Add MCP/connectivity without confirming with the user, introducing security risk
- Fail to distinguish between Active and Passive governance modes, defaulting to ad-hoc
  harness evolution without a documented protocol
- Create HARNESS_EVOLUTION.md for short-lived projects where it adds no value
- Miss the signal that a repeated behavior (≥ 3 occurrences) should be distilled into
  a project-specific skill
- Skip the anti-rot requirement: modifying project behavior without updating the
  corresponding harness files in the same change
- Omit a consistency layer entirely, or in skill-based form create one monolithic
  sync skill instead of one dedicated skill per concern — per-concern skills load
  automatically via their descriptions and are more precise and maintainable
- Create an AGENTS.md that fails to inform agents about harness architecture layer
  files — folder pointers are sufficient when a domain has many files, but each layer
  must be discoverable; exhaustive listing of individual files is not required
- Unnecessarily update AGENTS.md when creating skills from the 3× rule — agent
  frameworks discover and load skills automatically via their `description` field; no
  when-to-read-what entry is needed for newly created skills
- Not know the standard KB file taxonomy (REFERENCES.md, PLAN.md, WORKFLOW.md,
  SPEC.md, QUALITY.md) and their single-file vs folder selection rules
- Confuse ARCHITECTURE.md and DESIGN.md as optional extras rather than recognized
  root-level convention files with specific purposes

## Scope

One coherent work unit: one project harness, from initial assessment through a
working first version or a targeted improvement. Scope includes:

- Scanning the project and classifying its type using the Intensity Matrix
- Assessing the current harness health (missing, outdated, or excess components)
- Planning and executing harness changes (create, update, remove components)
- Setting up or updating the governance model (Active or Passive)
- Setting up a consistency layer appropriate to the project's complexity
- Providing security-compliant MCP configuration when requested and confirmed

Out of scope:

- Domain content for project-specific skills — the agent facilitates structure;
  domain knowledge must come from the user or existing project artifacts
- Implementing production code changes
- CI/CD pipeline design beyond harness-related validation scripts

## Content Boundaries

**Include in `SKILL.md` body (loaded on every invocation):**
- Architect persona and three core design principles
- Seven-step workflow (scan → classify → assess → plan → confirm → execute → verify)
- Harness Intensity Matrix (4-row quick-reference table)
- Component quick reference with conditional load pointers to assets and references
- Governance mode selection logic (table + mode descriptions)
- Security invariants (MCP confirmation requirement)
- Gotchas

**Load from `references/` only when the specific branch is entered:**
- `thick_harness_components.md` — when project is classified as Thick; detailed
  component specs (AGENTS.md layout rules, project Skill structure, KB file taxonomy
  with External Refs/Plans/Workflows/Specs/Quality, root-level convention files,
  Hooks)
- `sync_layer.md` — when setting up a reference-based consistency layer for a
  Medium-complexity project; sync reference file structure and AGENTS.md connection
- `connectivity_mcp_security.md` — when adding any MCP/connectivity component;
  security constraint template and risk checklist
- `active_governance.md` — when governance mode = Active OR when creating a
  skill-based consistency layer; skill refinement criteria, anti-rot sync protocol,
  harness-sync meta-skill (creates per-concern specialized sync skills), evolution
  log maintenance

**Load from `assets/` when creating the corresponding file type:**
- `agents_md_template.md` — when creating or fully restructuring AGENTS.md
- `harness_evolution_template.md` — when initializing HARNESS_EVOLUTION.md
- `project_skill_template.md` — when distilling a repeated behavior into a new skill
- `knowledge_entry_template.md` — when creating a new knowledge base document

## Gotchas Source

All gotchas in `SKILL.md` come from confirmed harness failure modes:

1. Outdated AGENTS.md after a refactor → agents operate on stale context, producing
   incorrect file paths, missing conventions, or referencing removed components
2. AGENTS.md exceeding 150 lines → full content read on every invocation, consuming
   token budget disproportionately across the agent's entire session
3. MCP configuration without user confirmation → unauthorized external access exposure
4. Creating harness components "for the future" → violates lean architecture; adds
   maintenance burden with no current value
5. Governance mode undocumented → future agents default to passive; active evolution
   protocol is silently lost after the originating conversation ends
6. HARNESS_EVOLUTION.md on a one-off project → meaningless overhead with no
   long-term beneficiary
7. Repeated behavior not extracted into a skill → same instructions regenerated on
   every invocation; inconsistent output across runs as instructions drift
8. Skill files placed outside `.agents/skills/` → agents cannot find them via
   standard discovery paths; cross-project deployment breaks
9. No consistency layer defined, or skill-based layer uses one monolithic skill
   instead of per-concern dedicated skills → harness drifts silently from
   implementation; individual sync skills are more precise and load automatically
   via their descriptions
10. AGENTS.md uses exhaustive file listing instead of layer-level pointers →
    budget consumed by enumeration instead of navigation; folder pointers are
    sufficient — the goal is to inform agents that the layer exists, not list files
11. Adding MCP in Active mode without explicit user authorization → security
    guardrail breach; MCP must never be added in either Active or Passive mode
    without explicit user confirmation — it expands agent capability boundaries
    beyond original scope

## Quality Bar

A harness produced with this skill passes if:

- AGENTS.md is within line budget (≤ 150 lines hard limit)
- Component selection matches the Intensity Matrix classification for the project type
- Governance mode is explicitly documented somewhere in the harness
- MCP components were created only after explicit, documented user confirmation
- All harness file cross-references resolve (no orphaned pointers)
- Anti-rot requirement is documented: functional changes must update harness files
