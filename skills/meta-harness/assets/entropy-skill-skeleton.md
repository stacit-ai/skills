---
name: harness-entropy-review
description: >
  Find stale, duplicated, contradictory, invisible, or excessive harness content. Use
  when reviewing long-lived harness health, after repeated drift findings, or before
  major harness cleanup.
---

# Harness Entropy Review

## Scan Scope

- [Entrypoints.]
- [Knowledge files or reachable endpoints.]
- [Project skills.]
- [Workflow and validation guidance.]

## Workflow

1. Identify stale references and invalid paths.
2. Identify duplicated or contradictory instructions.
3. Identify important content that is not discoverable.
4. Identify components with no current trigger or owner.
5. Report findings with keep/update/remove recommendations.
6. Apply only approved, source-of-truth-backed, or unambiguous changes.
7. Verify links, line budgets, and validation commands.

## Gotchas

- Prefer reporting uncertain removals over deleting potentially valid constraints.
