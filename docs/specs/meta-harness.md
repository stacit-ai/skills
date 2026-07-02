# Spec: meta-harness

## Purpose

`meta-harness` guides an agent through designing, auditing, and improving a project
harness: the agent-visible environment, constraints, tools, and accessible knowledge
that help coding agents match user expectations.

This is one coherent skill. It should not split into multiple public skills. The main
`SKILL.md` carries high-frequency/default behavior so an agent can choose the
appropriate harness thickness and create a proportional baseline without loading any
reference. References exist only for low-frequency, complex, or meaningfully separate
paths.

## Trigger Conditions

Explicit triggers:

- set up a harness for this project
- create or update AGENTS.md
- improve the agent setup
- audit or repair the harness
- make project knowledge discoverable to agents
- add a project-specific skill
- create a sync or maintenance mechanism for harness content
- calibrate agent autonomy or approval boundaries

Indirect triggers:

- how should agents work in this project
- the agent does not know our conventions
- agents keep missing project context
- help structure the agent context
- make the agent setup less stale or easier to maintain
- decide what instructions, tools, or checks agents need

## What The Agent Lacks

Without this skill, agents tend to:

- put too much detail into always-read entrypoints
- ask users questions that can be answered by inspecting the repo
- treat conversation history, global personal skills, or team habit as if future
  project agents can see them
- create speculative harness components that have no current use
- split reference files by topic even when the files are short or always loaded
- choose storage or workflow mechanisms before understanding project needs
- default to autonomous evolution or multi-agent systems without explicit delegation
- assume agents may initiate workflow state changes without knowing human handoff rules
- produce opaque quality checks that do not tell agents why a failure matters or what
  to try next
- treat minimum harness thickness as the goal instead of choosing by project facts and
  risk
- select or avoid L2 by bias instead of using the maturity checklist and user
  requirements
- apply the same thickness to every harness layer instead of calibrating each layer
- omit project-visible sync/update rules, causing harness drift

## Scope

In scope:

- assessing the current project and existing harness
- creating a proportional L0, L1, or L2 harness based on project facts
- creating or revising entrypoints, local knowledge, constraints, validation, workflow
  guidance, sync/update rules, and maintenance guidance
- using structural skeletons and snippets as implementation starting points
- designing L3/L4 only after explicit user intent
- recording known human involvement, delegated workflow authority, and handoff
  boundaries when they affect harness behavior

Out of scope:

- creating additional public skills in this repository
- binding generic harness instructions to a specific provider, platform, repository
  host, task system, communication tool, or remote storage backend
- making project harness depend on this global `meta-harness` skill being available
  to future agents
- enabling external access, workflow automation, or autonomous operation without
  explicit team delegation
- treating agent-failure-driven knowledge or reference updates as ordinary L0-L2 sync
  behavior

## Content Boundaries

`SKILL.md` includes behavior needed on most runs:

- harness definition and visibility boundary
- warning that global `meta-harness` is not project harness
- minimal discovery checklist
- checklist-based target maturity choice for L0, L1, or L2
- single-agent as the default topology for ordinary harnesses
- human involvement and workflow delegation boundaries
- per-layer thickness guidance using omitted, light, medium, and thick
- default AGENTS.md-first entrypoint and local knowledge-library guidance, with local
  agent-first knowledge entries under project-root `./.agents/knowledge/`
- architecture-level project map guidance, unless a discoverable architecture document
  already provides the map
- default proportionate constraints and validation guidance
- actionable diagnostics for quality tools and validation commands
- lightweight stale-content guidance for durable harnesses
- plan output requirements and gotchas

`references/` is not a topic encyclopedia. A reference file is justified only when the
path is low-frequency or complex enough that loading it on ordinary harness creation
would waste context. If a branch is almost always loaded, it belongs in `SKILL.md`.
If a reference is short and generic, merge it into `SKILL.md` or a larger branch
manual.

The current reference set is:

- `audit-existing-harness.md` for audit, repair, slimming, modernization, or conflict
  cleanup of an existing harness.
- `external-knowledge-carrier.md` for non-local sources of truth, registered tools, or
  reachable endpoints.
- `project-skill.md` for repeated, fragile, order-sensitive, or branchy project
  procedures that warrant a project skill.
- `sync-and-maintenance.md` for non-trivial sync, long-term cleanup, or entropy
  mechanisms beyond the inline update rule; L0-L2 sync remains source-of-truth driven.
- `advanced-autonomy.md` for explicit L3/L4, self-evolution, unattended operation,
  autonomous routing, persistent memory, multi-agent design, or agent-failure-driven
  knowledge/reference updates.

`assets/` contains only structural skeletons or copyable snippets. Assets must not
contain filled project examples, provider-specific examples, implementation logic, or
decision rules.

Knowledge-library assets are split by document type, not collapsed into one generic
entry template:

- `knowledge-quality-skeleton.md`
- `knowledge-references-skeleton.md`
- `knowledge-workflow-skeleton.md`
- `knowledge-plan-skeleton.md`
- `knowledge-goals-skeleton.md`

These knowledge templates must not each include their own `Keep In Sync` section.
Knowledge-library updates are governed by one project-visible sync/update rule,
workflow, or sync skill.

## Quality Bar

The skill passes if:

- a basic L0-L2 harness can be created from `SKILL.md` alone
- the agent can choose L0, L1, or L2 from the maturity checklist, project facts, and
  user requirements without automatically selecting or avoiding L2
- the default ordinary harness remains single-agent
- workflow automation and human handoff boundaries are recorded only from team
  decisions, not assumed
- quality tools and validation guidance provide actionable diagnostics for agents
- the plan reports each relevant harness layer as omitted, light, medium, or thick
- references are substantial low-frequency or complex branch manuals
- no branch-loading table is used as the main structure
- short/default guidance is in `SKILL.md`, not isolated in tiny references
- local agent-first knowledge defaults to a project-root `./.agents/knowledge/`
  library of files or folders, not a single document
- local knowledge entries are discoverable from AGENTS.md or an equivalent entrypoint
  rule and loaded only when relevant
- knowledge template assets are split by common document type rather than using one
  generic knowledge-entry template
- knowledge template assets do not repeat `Keep In Sync`; the harness uses one
  discoverable sync/update rule or mechanism for knowledge-library maintenance
- project harness generated by this skill carries future-agent discoverability and
  sync/update rules independently of global `meta-harness`
- AGENTS.md is preferred as the global agent context; CLAUDE.md duplicates are avoided
  by pointing to AGENTS.md unless the team explicitly uses Claude Code only
- a dedicated sync skill does not require a duplicate AGENTS.md Keep In Sync section
- failure-driven reference or knowledge updates are limited to L3/L4 or explicitly
  authorized self-maintenance
- the AGENTS.md skeleton uses an architecture-level project map and marks sync content
  as removable when a sync skill is used
- no concrete provider, task tool, messaging tool, repository host, or storage backend
  example appears in the skill body or generic references
- the skill can produce a harness plan listing layers, files or reachable endpoints,
  create/update/remove actions, validation, and assumptions
