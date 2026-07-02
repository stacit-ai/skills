# Project Skill

Load this when a repeated, fragile, order-sensitive, or branchy project procedure
should become a project skill.

## When A Skill Is Warranted

Create a project skill when ordinary entrypoint text or a workflow note is not enough:

- the procedure has several ordered steps
- agents have repeated the same non-obvious instructions
- a workflow has branch-specific references or assets
- mistakes would be expensive or hard to detect
- the trigger can be described clearly enough for future agents

Do not create a skill for a one-off task, stable background knowledge, or a short rule
that belongs in the entrypoint.

## Authoring Process

1. Load [assets/project-skill-skeleton.md](../assets/project-skill-skeleton.md).
2. Define one coherent work unit. If the procedure has two unrelated triggers, split
   it or use a simpler workflow file.
3. Write the description around user intent and project conditions, not around file
   names alone.
4. Put always-needed workflow in the skill body.
5. Add skill-local references only for substantial branches that are not normally read
   together.
6. Add assets only for structural skeletons or snippets the skill will copy.
7. Add gotchas for project-specific non-obvious failure modes.

## Content Placement

Put content in the project skill body when it is needed on most invocations of that
skill. Put content in the project skill's references only when the skill itself reaches
a meaningful branch that many invocations will skip. Put assets in the project skill
only for structural snippets or skeletons the skill will copy.

Do not put broad project goals, architecture summaries, or team workflow rules into a
project skill just because the skill is being created. Those belong in entrypoints,
knowledge files, or workflow docs unless they are specific to the skill's task.

## Discoverability

The project harness must explain how project skills are discovered in the team's agent
environment, or the entrypoint must point agents to the skill location. Do not assume
the global meta-harness skill is available to future agents.

If the team relies on automatic skill discovery, the project harness should still make
the skill system discoverable at a high level. If the framework does not reliably
inject project skills, add an entrypoint pointer.

## Quality Check

Before creating the skill, verify:

- the trigger is clear
- the procedure has a stable source of truth
- the skill does not duplicate an existing entrypoint or workflow rule
- any references and assets are loaded under precise conditions
- the project has a way to keep the skill current when the underlying workflow changes

## Sync Rule

Every project skill should have an obvious update trigger. Add or point to a
project-visible rule for what happens when the procedure, paths, commands, validation,
or source of truth changes. A skill without an update path becomes stale silently.
