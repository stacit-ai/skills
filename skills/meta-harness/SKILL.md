---
name: meta-harness
description: >
  Design, audit, and improve agent harnesses: the environment, constraints, tools,
  and accessible knowledge that help coding agents match user expectations. Use
  when setting up agent instructions, creating or editing AGENTS.md, making project
  knowledge discoverable, adding project skills, designing sync or maintenance
  mechanisms, calibrating agent autonomy, or reviewing why agents miss project
  conventions.
---

# Meta-Harness

A harness is the agent-visible environment, constraints, tools, and accessible
knowledge that make agents match user expectations. It expands agent capability with
environment, information, and tools, then narrows the implementation space with
proportionate target, architecture, quality, and workflow constraints.

This skill is only a design aid. It may exist in one user's global skill library while
other teammates and future agents cannot see it. Any rule that future agents must
follow belongs in the project's reachable harness: repo-connected files, project
skills, registered tools, validation commands, or reachable endpoints.

## Core Rules

- Important information must be accessible to future agents. Conversation history,
  private chat, and team habit are not durable harness.
- Inspect discoverable project facts before asking the user. Ask only for team
  decisions, access boundaries, or facts that cannot be found locally.
- Create only components that satisfy current concrete needs.
- Keep entrypoints short and navigational. Detailed rules belong behind pointers.
- Choose the maturity level from user requirements, project facts, and risk. Keep
  components proportionate; thinness controls cost, but is not the goal.
- Default to one agent. Consider multiple agents only when the user asks for it or
  when designing advanced autonomy.
- Do not add commit, PR, review, merge, task-state, notification, or other workflow
  automation unless the team has explicitly delegated that action.

## Workflow

### 1. Establish The Visibility Boundary

Identify what future agents can actually discover. If an important project rule is
only in the prompt, current conversation, a personal global skill, private chat, or
team habit, encode it into project harness or point to a reachable source.

Every created harness must include or point to:

- where future agents start reading
- where project goals, architecture, conventions, and workflow rules live
- what validation commands or checks agents should run
- what must be updated when structure, commands, conventions, or workflows change

### 2. Inspect The Project

Read enough local state to avoid guessing:

- existing entrypoints and harness files
- repository layout and architecture documents
- README and project goal signals
- language, framework, package, and tool manifests
- development, test, deployment, and CI signals
- coding style, validation commands, and version-control conventions
- human involvement level, delegated workflow actions, approval boundaries, and handoff
  expectations
- recent git history when it clarifies lifecycle or workflow

When the task is primarily audit, repair, slimming, modernization, or conflict cleanup
of an existing harness, read
[references/audit-existing-harness.md](references/audit-existing-harness.md). For
normal baseline creation or targeted updates, continue with this file.

### 3. Choose The Practical Target

Use the checklist below to choose the target maturity. User requirements can set a
minimum or target level; project facts and risk decide whether that level is adequate.
Do not downgrade just to stay lightweight or upgrade just to appear more robust.

Select the level that matches the evidence:

- L0: prompt-only or temporary guidance. Use for occasional questions, trivial
  changes, or low-risk one-off work where durable instructions would add more cost
  than value.
- L1: a short durable entrypoint plus minimal validation or constraints. Use when
  agents will return to the project, but the project is simple, low-risk, or mostly
  human-written.
- L2: a feedback loop with stronger validation, workflow constraints, and explicit
  sync/update rules. Use when the project is maintained, collaborative, agent-driven
  for substantial implementation, has public or user-visible contracts, is costly to
  break, changes frequently, or the user asks for durable tests, CI, workflow rules,
  or sync/maintenance.
- L3: self-maintaining harness with durable memory, autonomous upkeep, and audited
  feedback.
- L4: multiple agent roles with explicit context boundaries and coordination rules.

Report the checklist evidence for the chosen level. If evidence points to L2, select
L2 unless the user deliberately limits scope; if evidence does not support L2, explain
why L0 or L1 is sufficient.

Default to a single-agent harness for L0-L2. Do not introduce role-split agents,
self-maintenance, or autonomous workflow operation unless the user explicitly asks for
advanced autonomy or the project already has project-visible authority for it.

Read [references/advanced-autonomy.md](references/advanced-autonomy.md) only when the
user explicitly asks for self-evolution, persistent memory, unattended operation,
autonomous task routing, multi-agent design, agent-failure-driven knowledge updates,
or L3/L4.

### 4. Create Or Revise The Entrypoint

Prefer AGENTS.md as the project-wide agent context. Use CLAUDE.md by itself only when
the team explicitly says the project is for Claude Code only. If both AGENTS.md and
CLAUDE.md are needed, keep AGENTS.md as the source of truth and make CLAUDE.md refer
to it instead of duplicating rules.

Use [assets/agents-md-maximal-skeleton.md](assets/agents-md-maximal-skeleton.md) when
creating or substantially restructuring AGENTS.md. Start from the maximal empty
structure, fill only sections backed by current facts or user decisions, then delete
every section that does not serve the project.

Skip durable entrypoint creation for L0 unless the user explicitly asks for one. For
L1+, the entrypoint is the normal discovery root.

The final entrypoint should be short and navigational. Include:

- project purpose
- an architecture-level project map unless another discoverable architecture document
  already provides it
- important reachable context
- core conventions that apply to most tasks
- when-to-read-what pointers
- validation commands
- approval or safety boundaries that apply to most tasks
- a small sync/update rule or pointer to the project-visible sync mechanism, unless a
  sync project skill is the chosen mechanism

Keep the project map shallow: enough to tell agents where to explore, not a full file
inventory. A map that changes on routine file additions is too detailed.

### 5. Add Local Knowledge Library Only When Needed

Create a local agent-first knowledge library only when the entrypoint would become too
long or when agents need focused documents with precise load conditions. The default
local knowledge root is `./.agents/knowledge/` at the project root. It is a set of
files or folders, not one catch-all document.

Only create categories the current project needs. Do not create empty knowledge
folders or placeholder documents. Make every knowledge entry discoverable from
AGENTS.md through `When To Read What` or an equivalent entrypoint rule so agents load
it only when relevant.

Use the matching asset when creating a local knowledge entry:

- Quality control: [assets/knowledge-quality-skeleton.md](assets/knowledge-quality-skeleton.md)
- References: [assets/knowledge-references-skeleton.md](assets/knowledge-references-skeleton.md)
- Workflow: [assets/knowledge-workflow-skeleton.md](assets/knowledge-workflow-skeleton.md)
- Plan: [assets/knowledge-plan-skeleton.md](assets/knowledge-plan-skeleton.md)
- Goals or requirements: [assets/knowledge-goals-skeleton.md](assets/knowledge-goals-skeleton.md)

Prefer existing maintained project docs when they are accurate and concise. Do not
duplicate external truth locally unless the project needs an offline copy, a pinned
snapshot, or a concise agent-facing summary. When important context should live
outside repo-local docs or the source of truth is a registered tool or reachable
endpoint, read
[references/external-knowledge-carrier.md](references/external-knowledge-carrier.md).

### 6. Calibrate Layer Thickness

For each harness layer, choose `omitted`, `light`, `medium`, or `thick`. Omit a layer
when no current need proves its value. Use light guidance when a sentence or pointer
is enough. Use medium when agents need a dedicated file, workflow, or validation path.
Use thick only when enforcement, richer tooling, or repeated loading cost is justified
by project risk or maintenance needs.

Record the known human involvement level before adding workflow constraints: Q&A,
command assistance, implementation assistance, PR/task handoff, or autonomous
maintenance. If the level is unknown, assume humans keep ownership of approvals,
integration, and external workflow state.

- Environment: weaker isolation needs clearer approval and safety boundaries; stronger
  isolation can support more autonomous agent work. Record only boundaries future
  agents need.
- Target constraints: most durable harnesses need at least a goal statement. Add
  thicker product, interface, visual, or behavior constraints only when the project
  has such contracts.
- Implementation constraints: keep one-off and exploratory work thin. Use thicker
  architecture, module, dependency, and design-direction guidance for complex or
  long-lived projects.
- Quality constraints: calibrate tests, lint, formatting, validation commands, review
  gates, and repository-safety constraints by error cost, maintenance horizon,
  existing language or tool guarantees, and runtime/token cost. Custom quality tools
  must explain what failed, why it matters, and the likely fix or next command.
- Workflow constraints: record only team-decided planning, commit, PR, review, merge,
  handoff, task-state, and approval rules. Do not invent automation, notifications, or
  status transitions.
- Information tools: add references, knowledge files, registered tools, or reachable
  endpoints only when they expand current agent capability and can be discovered by
  future agents.
- Workflow tools: add only when the team has delegated workflow actions and access is
  authorized. Otherwise document the human handoff.
- Capability tools: add only when they are needed for current development, validation,
  inspection, or debugging work.
- Repository safety constraints: calibrate around leak risk and collaboration boundary;
  focus on preventing secrets or private data from entering the repository.

Validation should help agents self-correct: say what failed, why it matters, where
the source of truth is, and what to run or inspect next. This applies to validation
commands, custom linters, formatters, tests, and quality scripts. Do not add expensive
checks or custom tools unless they protect a current need.

### 7. Capture Repeated Procedures

Keep simple rules in the entrypoint or a knowledge file. Read
[references/project-skill.md](references/project-skill.md) when a project procedure is
repeated, fragile, order-sensitive, or too branchy for ordinary docs.

Project skills created from this process must be discoverable by future agents through
the project's skill mechanism or entrypoint pointers. They must not depend on this
global meta-harness skill remaining available.

### 8. Keep The Harness Current

Any durable harness should tell future agents what content can become stale. For
lightweight projects, one sentence in the entrypoint is enough. Use a table, workflow,
or project skill only when the project is maintained, multi-artifact, or repeatedly
changed.

For L0-L2, sync and maintenance are source-of-truth driven: when a visible file,
command, interface, workflow rule, or reachable endpoint changes, update dependent
harness content. Do not make ordinary L0-L2 harnesses update references or knowledge
automatically from agent failures. Failure-driven knowledge/reference updates require
L3+ review or explicitly authorized self-maintenance.

If synchronization is handled by a project skill, do not also create a Keep In Sync
section in AGENTS.md. Avoid duplicate rules; only ensure future agents can discover
the skill through the project's skill mechanism or an entrypoint pointer if discovery
is not automatic.

```markdown
## Keep In Sync

| When this changes | Update |
|---|---|
| Project structure or entry commands | AGENTS.md and related knowledge pointers |
| Public interfaces or user-visible behavior | Specs, examples, tests, and agent guidance |
| Validation commands or workflow rules | AGENTS.md validation/workflow sections |
```

Read [references/sync-and-maintenance.md](references/sync-and-maintenance.md) when
sync becomes multi-step, recurring, cross-artifact, or when the project needs long-term
cleanup for stale, duplicated, contradictory, or excessive harness content.

### 9. Produce And Verify

When planning or finishing harness work, report:

- affected harness layers
- target maturity level
- known human involvement level and delegated workflow authority
- agent topology, normally single-agent
- each layer's thickness: omitted, light, medium, or thick
- files, project skills, registered tools, or reachable endpoints changed
- create/update/remove actions
- why a thicker harness was not chosen, when that is non-obvious
- validation steps
- assumptions and user decisions still needed

Verify that future agents can discover the relevant rules without this conversation or
this global skill. Check local links, validation commands, entrypoint length, and
whether sync/update rules are present in project-visible harness.

## Gotchas

- If future agents cannot discover information, it is not project harness.
- Stale harness content is worse than absent harness content because it makes agents
  confidently follow wrong instructions.
- Do not name ordinary principles with invented labels. Use direct instructions.
- Do not copy examples from a user's explanation into generic skill text.
