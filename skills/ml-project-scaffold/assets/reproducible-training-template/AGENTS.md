# AGENTS.md

## Project Shape

This is a reproducible ML training/evaluation project. Keep workflows repeatable and
maintainable without adding service-grade robustness or heavy architecture.

## When To Read What

- Read `.agents/knowledge/WORKFLOW.md` before changing training, evaluation, data
  preparation, command workflows, or expensive manual checks.
- Read `.agents/knowledge/QUALITY.md` before editing code, tests, data handling,
  outputs, pre-commit, or CI.
- Read `.agents/knowledge/REFERENCES.md` when selecting or updating external ML,
  Python, or tooling documentation links.

## Structure

- The package created by `uv init` contains project logic.
- Create a workflow submodule inside that package when workflow modules should be
  exposed through `justfile`.
- `configs/` stores experiment configuration.
- `data/raw/` stores immutable raw inputs.
- `data/interim/` stores intermediate artifacts shared between steps.
- `data/processed/` stores final data products.
- `outputs/` stores run artifacts and is ignored by git.
- `scripts/` stores self-contained helper scripts only when commands are too complex
  for `justfile`.
- `notebooks/` is for human exploration.
- `tests/` contains targeted lightweight tests.

## Commands

Use `just` as the command surface. Run `just` to list commands.

## Commits

Use Conventional Commits. Skill-free project changes may omit scope, e.g.
`feat: add baseline evaluation`.
