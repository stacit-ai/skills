# Spec: git-commit

## Purpose

Guides an agent through the full workflow of creating an atomic, well-described git
commit: discovering project conventions, analyzing change atomicity, scanning for
sensitive data, verifying pre-commit hooks, running CI checks, drafting a compliant
commit message (50/72 rule), and executing the commit.

## Trigger Conditions

**Explicit:**
- "make a commit"
- "git commit"
- "commit my changes"
- "commit this"
- "create a commit"
- "stage and commit"
- "commit and push"
- "create a commit message"

**Indirect (must also trigger):**
- "save my changes to git"
- "checkpoint my work"
- "submit my code"
- the user asks to create a commit message and run git

## What the Agent Lacks

Without this skill, an agent would likely:
- Skip checking project configuration files and produce a message that violates
  project-specific conventions
- Commit non-atomic changes without offering to split them
- Omit security scanning of the diff, potentially committing sensitive data
- Skip pre-commit hook verification, causing unexpected hook failures at commit time
- Bypass hooks with `--no-verify` as a shortcut when they fail
- Produce a message that violates the 50/72 character rule
- Use past tense or third-person instead of imperative mood
- Explain implementation details ("how") instead of motivation ("why") in the body

## Scope

One coherent work unit: one or more commits (split from a single staged change set)
that follow all project conventions and quality gates.

Out of scope:
- Formatting the commit message for a specific convention (conventional-commits or
  gitmoji skills handle that)
- Pushing the commit or creating pull requests

## External Dependencies

None. `validate_commit_msg.py` uses only Python stdlib (no third-party packages).
