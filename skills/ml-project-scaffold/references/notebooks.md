# Notebook Integrations

Read this file only when the project will use Jupyter or marimo. Decide whether the
notebook is disposable exploration, a project workflow, or a versioned executable
artifact before adding dependencies or commands.

## Jupyter

- For read-only access to a uv project's environment, run Jupyter as an isolated tool:
  `uv run --with jupyter jupyter lab`.
- Add `ipykernel` as a development dependency and create a named project kernel when
  notebook cells must install into or mutate the project environment. Select that
  kernel explicitly in Jupyter or VS Code.
- Prefer `uv add <package>` when a notebook dependency belongs to the project. A plain
  `uv pip install` changes an environment without recording the dependency in
  `pyproject.toml` or `uv.lock`.
- Without a project kernel, `!uv pip install` can target Jupyter's temporary environment
  and disappear when the server exits. Do not present that as a reproducible setup.
- Use `uv tool run jupyter lab` only for ad hoc, non-project exploration.

## marimo

- Prefer a project dependency and `uv run marimo edit <notebook.py>` when the notebook
  imports project code or should share the project lockfile.
- For a self-contained notebook, add dependencies with
  `uv add --script <notebook.py> <package>` and edit it with
  `uvx marimo edit --sandbox <notebook.py>`. Keep the inline script metadata committed.
- Use `uvx marimo edit` only for disposable exploration. When marimo is injected with
  `uv run --with marimo`, packages installed from its UI may not persist in the project.
- Run a versioned marimo notebook non-interactively with `uv run <notebook.py>`.

## Generated Harness

Record the chosen notebook mode, dependency-update command, kernel or sandbox command,
and whether notebooks are executable project artifacts. Do not add both Jupyter and
marimo unless the project requires both.

## Sources

- https://docs.astral.sh/uv/guides/integration/jupyter/
- https://docs.astral.sh/uv/guides/integration/marimo/
