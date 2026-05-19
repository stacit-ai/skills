# Spec: gitmoji

## Purpose

Guides an agent through selecting the correct gitmoji emoji and drafting a commit
message that follows the gitmoji specification. Covers emoji selection, short vs.
long format, scope rules, and breaking change notation.

## Trigger Conditions

**Explicit:**
- "use gitmoji"
- "write a gitmoji commit message"
- "what emoji should I use for this commit"
- "format this as a gitmoji commit"

**Indirect (must also trigger):**
- `git log` shows messages that begin with an emoji character or `:emoji-code:`
- the project's `CONTRIBUTING.md` mentions gitmoji
- the user asks for an emoji in their commit message

## What the Agent Lacks

Without this skill, an agent would likely:
- Pick a plausible-looking emoji that does not correspond to an official gitmoji entry
- Use the text code (`:bug:`) when the project uses the unicode character (🐛) or vice versa
- Combine an emoji with a type prefix (`feat: ✨ add feature`) when that is not the
  project's convention
- Miss the full gitmoji vocabulary, leading to overuse of a few common emojis

## Scope

One coherent work unit: drafting one gitmoji-formatted commit message.

Git mechanics (staging, hooks, CI) are out of scope — covered by the git-commit skill.

## External Dependencies

- Gitmoji specification: https://gitmoji.dev/specification
- Gitmoji full emoji list: https://gitmoji.dev/
