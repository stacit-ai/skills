# WORKFLOW.md

## Command Surface

Use `just` for repeatable commands. Keep command recipes short; move complex helper
logic to `scripts/` only when it would make the command runner hard to read.

## Setup

Default setup:

```sh
uv sync
uvx pre-commit install
```

Document GPU, CUDA, or accelerator-specific install notes here when the project chooses
a backend. Do not assume one GPU backend works on every machine.

## Training

Training workflows live under `_package_name_/workflows/` and are invoked through
`just train` or more specific project commands.

Training commands should fail early for unexpected state. Add dirty-data handling only
for known input issues where skipping or recording a small number of bad records is
more responsible than wasting an expensive run.

## Evaluation

Evaluation workflows live under `_package_name_/workflows/` and are invoked through
`just eval` or more specific project commands.

Evaluation outputs belong in `outputs/` or `data/processed/`, depending on whether they
are transient run artifacts or final data products.

## Data Preparation

Only deliberate data preparation commands may write generated artifacts. Never modify
`data/raw/` in ordinary training or evaluation workflows.

## Expensive Checks

Expensive smoke tests, GPU tests, and partial training runs are manual-only. Keep them
as explicit `just` commands and do not run them in pre-commit or default CI.
