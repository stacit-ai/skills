# QUALITY.md

## Shared Quality

- Keep training and service contracts explicit and versioned in repo files.
- Use pre-commit and CI for formatting, linting, secret checks, and lightweight tests.
- Do not run expensive training, GPU, model-download, or end-to-end service checks in
  default CI unless the project explicitly budgets for them.
- Do not commit secrets, `.env` files, raw private data, checkpoints, or run outputs.

## Training Quality

Training code follows reproducible training/evaluation rules: readable workflows,
targeted tests, immutable raw data, ignored outputs, and early failure for unexpected
states.

## Service Quality

Service code needs stronger maintainability and robustness than training scripts.
After a service framework is selected, document request/response validation, error
handling, configuration, observability, deployment, and compatibility rules in
`service/AGENTS.md`.
