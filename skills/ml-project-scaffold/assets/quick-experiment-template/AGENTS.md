# AGENTS.md

## Project Shape

This is a quick ML experiment repo. Optimize for fast iteration, readable scripts, and
clear results. Do not add heavy architecture, strict type checking, or broad test
requirements unless the project grows beyond experiment scope.

## Structure

- `train.py`, `eval.py`, and similar root files are workflow entrypoints.
- A project package stores shared code only when multiple workflows must use the same
  logic consistently. Create it only when needed.
- `configs/` stores coarse experiment settings.
- `data/` stores raw immutable input data.
- `notebooks/` is for human exploration.
- `outputs/` stores logs, checkpoints, predictions, and run artifacts; it is ignored by
  git and code must create it when needed.
- `scripts/` may be added for complex helper commands called by `justfile`.
- `tests/` is optional and targeted.

## Code Rules

- Prefer procedural workflow files with a self-documenting `main`.
- Workflow files are final entrypoints and should not be imported.
- Put shared logic in a project package only when divergent copies would create
  inconsistent behavior.
- Prefer readability over removing every repetition.
- Fail early for unexpected states. Handle dirty data defensively only for known cases
  where one bad record should not waste an expensive pipeline.
- Use docstrings for shared module code. Public or workflow-called interfaces document
  parameters, returns, and errors; private helpers can use a one-line purpose docstring.

## Data And Config

- Workflows must not modify `data/` except for explicit data preparation steps.
- Config values should represent experiment choices such as data path, model name,
  hyperparameters, and output path.
- Do not mirror every code module into config or use config to assemble the whole model.

## Commands

Use `just` as the command surface. Run `just` to list available commands.

Default dependency flow:

```sh
uv venv
uv pip compile requirements.in --output-file requirements.txt --no-annotate --no-emit-index-url
uv pip install -r requirements.txt --torch-backend=auto
uv pip install -r requirements.dev.txt
```

Automatic PyTorch backend selection is a local convenience for this experiment class;
it does not define a reproducible deployment backend.

Run formatting, linting, and tests through their direct `just` recipes. The default
`just check` runs formatting and linting checks; add tests only after they exist and are
consistently fast.

## Git And Quality

- Use Conventional Commits without scope by default, e.g. `feat: add baseline training`.
- Do not commit secrets, `.env` files, raw private data, or `outputs/`.
- Keep checks focused on repo safety and basic formatting. If Git hooks are enabled,
  keep their configuration, development dependency, and `just` commands consistent;
  run secret scanning after all file-changing hooks.
  Avoid heavy CI for this project class.
