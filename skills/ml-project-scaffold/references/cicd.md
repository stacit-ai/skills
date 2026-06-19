# CI/CD With uv

Read this file when creating or changing GitHub Actions or GitLab CI/CD. Generate only
the selected platform's configuration. Run quality tools directly in CI; do not use
`pre-commit run --all-files` as the CI command surface.

## Shared Rules

- Pin uv and third-party actions or images according to the repository's supply-chain
  policy. Install the Python version declared by `.python-version` or `pyproject.toml`.
- For uv projects, use `uv sync --locked --dev` and add only the extras required by the
  job. Use `--all-extras` only when no extras conflict.
- Key caches from `uv.lock`; use `requirements.txt` for a `uv pip` project. Prune
  persistent caches with `uv cache prune --ci`.
- Run format checks, lint, and fast tests as separate commands. Put GPU, model-download,
  training, and long smoke tests in explicitly triggered jobs.
- Use a CPU PyTorch extra on generic runners. Use accelerator extras only on runners
  whose driver, base image, and runtime contract are documented.

## GitHub Actions

Use this as the default uv project job, then adjust Python, extras, and commands to the
generated project:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v8
        with:
          version: "0.11.22"
          enable-cache: true
      - run: uv python install
      - run: uv sync --locked --dev
      - run: uv run ruff format --check .
      - run: uv run ruff check .
      - run: uv run pytest -m "not slow"
```

Use a Python matrix only when the project promises multiple supported versions. Use
repository secrets or trusted publishing for private dependencies and releases; never
put credentials in workflow files or dependency URLs.

## GitLab CI/CD

Use this as the default uv project job, then adjust the image, extras, and commands:

```yaml
variables:
  UV_VERSION: "0.11.22"
  PYTHON_VERSION: "3.12"
  BASE_LAYER: trixie-slim
  UV_LINK_MODE: copy
  UV_CACHE_DIR: .uv-cache

check:
  image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  cache:
    key:
      files:
        - uv.lock
    paths:
      - $UV_CACHE_DIR
  script:
    - uv sync --locked --dev
    - uv run ruff format --check .
    - uv run ruff check .
    - uv run pytest -m "not slow"
  after_script:
    - uv cache prune --ci
```

GitLab build directories are commonly separate mount points, so keep
`UV_LINK_MODE=copy`. If using a distroless uv image, clear its entrypoint explicitly.

## Generated Harness

Record the CI platform, Python and uv version sources, cache key, selected dependency
extras, direct quality commands, and which expensive checks remain manual.

## Sources

- https://docs.astral.sh/uv/guides/integration/github/
- https://docs.astral.sh/uv/guides/integration/gitlab/
- https://docs.github.com/llms.txt
- https://docs.gitlab.com/llms.txt
