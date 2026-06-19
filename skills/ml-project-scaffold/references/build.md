# Build Integrations

Read this file only when the project uses Docker for builds or deployment, or has
already selected Bazel as its build system. Docker and Bazel are optional; do not add
either merely because this reference exists.

## Docker

- Copy `uv` and `uvx` from an official, version-pinned Astral image. Use an image digest
  when the project requires reproducible or verified supply-chain inputs.
- Add `.venv` to `.dockerignore`. A virtual environment is platform-specific and must
  be created inside the image.
- Copy the lockfile and `pyproject.toml` before project source, then run
  `uv sync --locked --no-install-project` to cache dependencies. Copy the source and run
  the final `uv sync --locked` afterward.
- Use a BuildKit cache mount for uv and set `UV_LINK_MODE=copy` when the cache and target
  are on different filesystems. Use `--no-cache` when image size matters more than
  rebuild speed.
- Exclude development dependencies in runtime images. Use `--no-editable` when the
  final image should not depend on source paths.
- Match the base image, Python, system CUDA libraries, driver contract, and selected
  PyTorch extra. Do not assume a locally detected accelerator exists in the build or
  runtime environment.
- For uv workspaces, use `--frozen --no-install-workspace` only in the dependency layer
  where member metadata is not yet available, then use `--locked` after copying the
  complete workspace.

## Bazel

- Keep Bazel integration out of the scaffold unless the project already uses Bazel or
  the user explicitly selects it.
- Follow the selected Python ruleset's uv lock integration: `rules_py` and
  `rules_python` have different dependency-resolution interfaces.
- For authenticated package hosts on Bazel 7 or newer, authenticate with `uv auth`,
  configure a host-specific Bazel credential helper, and use an executable wrapper for
  `uv --preview-features auth-helper auth helper --protocol=bazel`.
- Never embed registry credentials in `.bazelrc`, lockfiles, or wrapper scripts.

## Generated Harness

Record the build target, base/runtime compatibility, selected PyTorch backend, lockfile
enforcement command, cache behavior, and any authenticated package hosts.

## Sources

- https://docs.astral.sh/uv/guides/integration/docker/
- https://docs.astral.sh/uv/guides/integration/bazel/
