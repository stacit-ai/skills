# AGENTS.md

## Project Shape

This repo keeps training/evaluation and inference/service code versioned together.
Treat it as multiple subprojects with shared goals, shared quality rules, and separate
local harness files.

## When To Read What

- Read `.agents/knowledge/GOALS.md` before changing cross-project behavior or model
  artifact contracts.
- Read `.agents/knowledge/WORKFLOW.md` before changing commands, release flow,
  training-to-service handoff, or integration tests.
- Read `.agents/knowledge/QUALITY.md` before editing code, tests, CI, security rules,
  or data/output handling.
- Read `.agents/knowledge/REFERENCES.md` when selecting or updating framework/tool
  documentation links.
- Read `training/AGENTS.md` before changing training/evaluation code.
- Read `service/AGENTS.md` before changing service code.

## Structure

- `training/` is the reproducible training/evaluation subproject.
- `service/` is the inference/service boundary. It starts framework-neutral.
- `tests/integration/` stores cross-project train/inference consistency tests.
- Root `.agents/knowledge/` stores shared conventions and contracts.

## Commands

Use root `justfile` as the repo command surface. Run `just` to list commands.

## Commits

Use Conventional Commits. Use a scope when it clarifies the affected subproject, e.g.
`feat(training): add dataset builder` or `fix(service): preserve tokenizer settings`.
