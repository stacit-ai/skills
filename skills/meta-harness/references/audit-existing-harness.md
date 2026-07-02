# Audit Existing Harness

Load this when the task is primarily audit, repair, slimming, modernization, or
conflict cleanup of an existing project harness.

## Audit Sequence

1. List the project-visible harness entrypoints, knowledge files, project skills,
   validation commands, registered tools, and reachable endpoints.
2. Confirm which files or endpoints future agents can discover without this global
   meta-harness skill.
3. Compare the harness against current project structure, commands, public behavior,
   workflow, and validation.
4. Classify each issue as stale, duplicate, contradictory, invisible, missing,
   excessive, over-thick, or orphaned.
5. Recommend keep, update, move, merge, or remove.

## Discovery Checklist

Start from the same files future agents will see. Follow entrypoint pointers before
opening unrelated docs. Then inspect likely harness locations and validation
configuration. Use git history only to clarify whether a harness rule reflects a
current convention or an abandoned one.

For each discovered harness artifact, record:

- how future agents find it
- what task or change should cause it to load
- what source of truth it depends on
- how it is validated or kept current

An artifact with no discovery path is invisible. An artifact with no source of truth is
likely to drift.

## What To Look For

- Entry points that are too long or fail to point to important harness layers.
- References to paths, commands, APIs, or workflows that no longer exist.
- Multiple files stating the same rule differently.
- Useful project knowledge that is not reachable from an entrypoint, project skill,
  registered tool, or known endpoint.
- Project skills or workflow docs with no current trigger.
- Validation commands that do not match the current project.
- Components added for possible future use but not tied to current work.
- Thick constraints on simple or one-off work, such as multi-file procedures, heavy
  validation gates, or dedicated skills where a short pointer would be enough.
- Workflow automation or external access rules not backed by explicit team decisions.
- Maintenance mechanisms whose running cost exceeds the drift risk they prevent.

## Decision Rules

- Update when the content is still needed but wrong or incomplete.
- Move when valid content is loaded too often or belongs behind a more precise trigger.
- Merge when separate files are normally read together and neither is large enough to
  justify separate loading.
- Thin when the rule is valid but the current project does not justify its operational
  cost. Replace heavyweight machinery with a shorter pointer, note, or validation
  command when possible.
- Remove only when the component is clearly obsolete, duplicated, or unsupported by a
  current need. Ask before removing content that appears intentionally maintained.
- Leave unchanged when the content is accurate, reachable, and proportionate.

Prefer merging over splitting when two harness files are normally read together and
neither has a distinct trigger. Prefer moving content out of the entrypoint when the
rule is valid but only applies to a narrow workflow.

## Repair Plan

For each proposed change, state:

- current problem
- source of truth used for the correction
- exact harness artifact to update
- whether a project-visible sync/update rule also needs to change
- validation method
- whether the repaired result is intentionally thinner than the previous harness

Do not use audit as permission for a broad rewrite. Keep edits tied to findings.

## Verification

After repair, verify:

- entrypoints point to every important harness layer or reachable endpoint
- deleted files no longer have cross-references
- validation commands still run or are clearly marked as requiring user-provided
  environment setup
- sync/update rules mention any harness artifact whose source of truth changed
- future agents can follow the harness without seeing this audit conversation
- any remaining thick component has a current lifecycle, risk, or team-workflow reason
