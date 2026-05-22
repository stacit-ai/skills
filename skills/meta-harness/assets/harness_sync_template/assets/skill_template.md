---
name: [concern]-sync
description: >
  Detect and fix drift between [insert source, e.g. spec/] and [insert target, e.g.
  src/]. Use when [insert source path] or [insert target path] are modified, when
  [insert event-based trigger, e.g. a code style convention is changed], or when
  asked to [insert intent phrase, e.g. "sync the API spec"].
---

# [Concern] Sync

[One sentence: what diverges and why it matters in this project.]

## Workflow

1. Read [insert source file or directory] and [insert target file or directory].
2. Identify drift: [insert what to compare, e.g. endpoint names, field types, exported
   constants].
3. Apply corrections to [insert target] to bring it in sync with [insert source].

[Add detection or correction steps as needed. Each step must name specific files.]

## Gotchas

- **[Non-obvious coupling]** — [why the agent would miss or mishandle this sync
  relationship, and what the correct behavior is for this project]

[Include only project-specific, non-obvious coupling facts.]
