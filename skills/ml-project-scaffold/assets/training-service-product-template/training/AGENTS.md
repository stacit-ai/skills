# AGENTS.md

## Project Shape

This subproject owns reproducible training and evaluation. Root harness owns shared
train/service contracts; this file owns training-specific structure and workflow rules.

## Structure

- The package created by `uv init` contains training project logic.
- Create a workflow submodule inside that package when workflow modules should be
  invoked from the root `justfile`.
- `configs/` stores experiment configuration.
- `data/raw/` stores immutable raw inputs.
- `data/interim/` stores intermediate artifacts.
- `data/processed/` stores final data products.
- `outputs/` stores run artifacts and is ignored by git.
- `scripts/` stores self-contained helper scripts only when command recipes become too
  long.
- `tests/` contains targeted lightweight tests.

## Rules

- Apply reproducible training/evaluation conventions.
- Keep workflow code readable and fail early for unexpected states.
- Use defensive dirty-data handling only for known cases where skipping or recording a
  small number of bad records prevents wasting an expensive run.
- Document artifact handoff assumptions in root `.agents/knowledge/GOALS.md`.
