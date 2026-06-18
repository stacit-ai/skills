# QUALITY.md

## Code Quality

- Prefer readable ML code over abstracting away every repetition.
- Extract shared components for logical consistency, not just because code repeats.
- Use type annotations for IDE help, but do not enable static type checking by default.
- Public or cross-module functions/classes need docstrings with parameters, returns,
  and errors. Internal helpers can use concise purpose docstrings.
- Add comments for long logical blocks, not obvious statements.
- Fail early for unexpected states.

## Tests

- Keep tests targeted and lightweight.
- Add tests for custom data formatting, model components, metrics, or other logic where
  correctness reduces future debugging scope.
- Do not require coverage targets by default.
- Mark expensive training, GPU, and smoke tests as manual-only.

## Data And Outputs

- `data/raw/` is immutable raw input.
- `data/interim/` stores intermediate workflow artifacts.
- `data/processed/` stores final datasets, predictions, or derived products.
- `outputs/` stores logs, checkpoints, and run artifacts; it is ignored by git.
- Code must create output directories when needed.

## Configuration

Use configuration for experiment choices that are expected to change: data source, base
model, hyperparameters, feature switches, and output locations. Do not mirror every
code module into config or use config as a model assembly language by default.

## Git Safety

Do not commit secrets, `.env` files, private raw data, checkpoints, or run outputs.
Pre-commit and CI should catch common formatting and repository-safety issues.
