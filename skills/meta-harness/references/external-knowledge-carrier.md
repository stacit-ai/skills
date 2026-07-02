# External Knowledge Carrier

Load this when important context should live outside repo-local entrypoints or docs,
or when the source of truth is a registered tool or reachable endpoint.

## Carrier Decision

Use an external carrier when:

- the maintained source of truth already lives outside the repository
- duplicating it locally would create stale copies
- the agent needs tool-backed read or write access rather than static text
- access boundaries, permissions, or freshness matter more than local convenience

Keep local files when:

- the information is stable enough to maintain in the repo
- offline or pinned context is needed
- the content is an agent-facing summary rather than the source of truth
- the team does not grant external access to agents

When uncertain, keep the project harness local and add a question for the user. Do not
invent an external carrier or assume access that the team has not granted.

## Required Project Harness Pointers

External context is not useful unless future agents can discover it. Put a pointer in
the project harness that states:

- what the external source represents
- when agents should consult it
- whether it is source of truth or supplementary context
- what access boundary or approval applies
- what local file, if any, summarizes or pins it

Do not rely on a personal tool configuration being present for other agents. If access
depends on a registered tool, the project harness must say what capability is expected
and when it is used, without embedding credentials.

## Local Summary Pattern

If agents need a local summary of external truth, make the summary explicit:

- name the external source as the source of truth
- state what the local summary covers and intentionally omits
- include the date or project milestone the summary reflects when useful
- add a sync/update rule for changes that should refresh the summary

Do not copy broad external material into the repository just to make it available.
Summarize only the decisions, constraints, or access instructions agents need.

## Avoid Stale Copies

When local and external content both exist, choose one source of truth. The other
artifact should either summarize with a timestamp/scope or point to the maintained
source. Add a sync/update rule if agents are expected to keep both aligned.

## Security And Privacy

Never place secrets, private tokens, or sensitive personal data in harness files. If
the external source may expose sensitive information, record the access boundary and
the approval requirement in project-visible harness.

## Verification

Before finishing, confirm:

- the entrypoint or loaded harness file tells agents when to consult the external
  source
- the project does not require this global meta-harness skill to know the source exists
- credentials and private values are not embedded
- any local summary has a clear update trigger
