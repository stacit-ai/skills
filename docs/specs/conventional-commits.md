# Spec: conventional-commits

## Purpose

Guides an agent through drafting a git commit message that complies with the
Conventional Commits 1.0.0 specification. Covers the type decision tree, short vs.
long format selection, scope rules, breaking change syntax, and a `.gitmessage`
template for projects that want to enforce the format.

## Trigger Conditions

**Explicit:**
- "write a conventional commit message"
- "format this as a conventional commit"
- "I use conventional commits"
- "create a CC-formatted message"
- "what type should I use for this commit"

**Indirect (must also trigger):**
- the project has a `commitlint.config.*` that references `@commitlint/config-conventional`
- `git log` shows messages prefixed with `feat:`, `fix:`, `chore:`, etc.
- the user asks for a commit message with a type prefix

## What the Agent Lacks

Without this skill, an agent would likely:
- Choose the wrong type (e.g., `refactor` for a performance optimization instead of `perf`)
- Use scope inconsistently with project conventions
- Fail to emit a `BREAKING CHANGE` footer when a public API is modified
- Not know when to use `!` vs. the footer form for breaking changes
- Produce a body that explains "how" instead of "why"
- Use the wrong footer token format (`Breaking Change:` instead of `BREAKING CHANGE:`)

## Scope

One coherent work unit: drafting one Conventional Commits-formatted message given a
description of staged changes.

Git mechanics (staging, hooks, CI) are out of scope — covered by the git-commit skill.

## External Dependencies

- Conventional Commits specification v1.0.0:
  https://www.conventionalcommits.org/en/v1.0.0/
