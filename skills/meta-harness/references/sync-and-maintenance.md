# Sync And Maintenance

Load this when the project needs a non-trivial sync or maintenance mechanism beyond a
small inline "when this changes, update that" rule.

Do not create a standing sync or entropy mechanism for simple one-off work. For thin
harnesses, record the one or two things most likely to become stale and stop there.

For L0-L2 harnesses, sync and maintenance are source-of-truth driven. A visible
project change, command change, workflow decision, or reachable endpoint change can
trigger updates to dependent harness content. Repeated agent failures may justify
findings and recommendations, but not automatic knowledge or reference edits.
Failure-driven knowledge/reference updates belong in
[advanced-autonomy.md](advanced-autonomy.md).

## Choose The Lightest Mechanism

Use an inline entrypoint rule when the mapping is short and applies to most agents.

Use a workflow entry when:

- the sync or cleanup concern is recurring
- the steps are mostly linear
- the content is too long for the entrypoint
- findings can be reviewed by a human before edits

Use a dedicated project skill when:

- the procedure is frequent, fragile, or branchy
- several artifacts must be compared or updated
- precise trigger loading will save context over time
- agents are expected to perform the procedure with little prompting

If the project is not long-lived, collaborative, or repeatedly modified by agents,
prefer inline rules or one-time cleanup over workflow or skill creation.

When using a dedicated sync skill, do not create a separate Keep In Sync section in
AGENTS.md for the same concern. Duplicating the rule creates drift. The project only
needs enough entrypoint or skill-system guidance for future agents to discover the
skill.

## Sync Workflow Entry

Use [assets/sync-workflow-section.md](../assets/sync-workflow-section.md) for a
lightweight sync concern. The entry must name:

- trigger change
- source of truth
- dependent harness artifact
- exact update steps
- verification step

Common sync categories include structure, public behavior, validation commands,
architecture decisions, workflow rules, project skills, and reachable knowledge
endpoints. Include only categories that apply to the project.

Do not add a workflow entry for every category. Add one only when the project has that
source of truth and agents are likely to change it.

## Sync Skill

Use [assets/sync-skill-skeleton.md](../assets/sync-skill-skeleton.md) when one sync
concern deserves a dedicated project skill. Create one skill per consistency concern;
avoid a generic "sync everything" skill because it loads too broadly.

The skill description should trigger on the source change. The body should compare
source of truth against dependent artifacts, update stale guidance, remove conflicts,
and verify links or commands.

## Entropy Cleanup

Use [assets/entropy-workflow-section.md](../assets/entropy-workflow-section.md) for
periodic or manually triggered cleanup when the process is linear.

Use [assets/entropy-skill-skeleton.md](../assets/entropy-skill-skeleton.md) when
cleanup is recurring, branchy, or expected to be agent-driven.

Inspect:

- stale paths and invalid commands
- duplicated or contradictory rules
- important content that is not discoverable
- overgrown entrypoints
- unused project skills or workflow entries
- obsolete references to tools or endpoints
- harness components that are thicker than the project currently needs

## Safety

Maintenance mechanisms must prefer findings before destructive edits. Delete only when
local evidence is current and unambiguous, or when the user approves the removal.
When cleanup is prompted by failed agent runs, report the repeated failure pattern and
recommended harness update before editing. Editing knowledge from failure history
requires explicit authorization or advanced autonomy controls.

Every sync or cleanup mechanism must be project-visible. Future agents should be able
to find when it runs, what it updates, and how it verifies completion without reading
this global meta-harness skill.
