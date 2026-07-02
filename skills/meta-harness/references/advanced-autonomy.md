# Advanced Autonomy

Load this only when the user explicitly asks for self-evolution, persistent memory,
unattended operation, autonomous task routing, multi-agent design, agent-failure-driven
knowledge updates, or L3/L4 harness.

## Maturity Model

- L0: prompt-only guidance.
- L1: durable entrypoint and basic validation.
- L2: feedback loop through tests, checks, workflow constraints, and sync/update rules.
- L3: self-maintaining harness with durable memory, autonomous upkeep, and audited
  feedback.
- L4: multiple agent roles with explicit context boundaries and coordination rules.

## Preconditions For L3

Do not design self-evolution unless the project has:

- strong environment isolation or explicit approval boundaries
- durable, accessible memory or planning source of truth
- validation that can catch harmful harness drift
- clear rules for what agents may change without human review
- approval and rollback rules for any autonomous knowledge or reference edits
- a way to audit autonomous harness changes

If any precondition is uncertain, treat it as missing. Ask the user before granting
autonomous change authority or external write access.

## L3 Feedback Loops

Agent failures may trigger proposed reference or knowledge updates only when the
project has durable memory, an audit trail, validation, and approval or rollback
rules. Without those controls, repeated failures can produce findings but must not
drive automatic self-evolution.

Failed runs should produce findings before modifying knowledge. Each proposed update
must cite the source failure pattern, the checked source of truth, and the verification
that shows the new guidance is correct.

## Preconditions For L4

Do not design multi-agent structure unless:

- the agent framework supports the required coordination
- the project is complex enough to benefit from role separation
- role boundaries are clear and do not duplicate ownership
- context isolation improves quality enough to justify coordination
- token, cache, and latency costs are acceptable
- quality control remains owned by humans or a clearly defined review mechanism

Do not add multiple roles to a small project only to mirror an organization chart.
Role separation is useful only when it reduces context pollution or improves review
quality enough to justify coordination overhead.

## Workflow Authority

Agent-initiated commit, review, merge, task-state, notification, or handoff actions
require explicit delegation. If delegation is absent or ambiguous, design the harness
to produce human-readable findings and handoff instructions instead of changing
external workflow state.

## Harness Requirements

Advanced autonomy cannot depend on this global meta-harness skill. The project harness
must record:

- autonomy boundaries
- approval and rollback rules
- durable memory location
- task routing rules
- validation and audit trail
- how self-maintenance updates are reviewed
- which workflow actions agents may initiate and which remain human-owned

It must also record how to stop or downgrade autonomy. A future agent needs a visible
fallback path when validation fails, permissions are missing, or the project enters a
high-risk change.

## Plan Output

An advanced autonomy plan must include:

- target maturity level and why L0-L2 is insufficient
- isolation and approval model
- durable memory or planning source
- agent roles or autonomous responsibilities
- validation and audit mechanism
- feedback loop rules for failed runs and knowledge updates
- delegated workflow actions
- rollback or downgrade process
- human review points

## Default Fallback

If any precondition is missing, design an L0-L2 single-agent harness and document what
would need to change before advanced autonomy is safe.
