# PyTorch Dependency Strategy

Read this file whenever the project uses PyTorch, especially when CPU, CUDA, ROCm, XPU,
CI, containers, or multiple developer machines are involved.

## Determine The Environment Matrix

Before adding PyTorch, establish:

- supported operating systems and CPU architectures
- supported Python versions
- CPU, NVIDIA CUDA, AMD ROCm, or Intel XPU targets
- exact accelerator versions supported by the target drivers and runtime images
- which targets must share one lockfile

Do not infer the project backend from the machine running the scaffold. Do not invent a
CUDA, ROCm, or XPU version when the deployment matrix is unknown.

## Reproducible uv Projects

Use mutually exclusive optional dependencies when one project must support selectable
backends on otherwise similar machines. Create only the extras the project supports,
for example `cpu` and a confirmed `cu130` target:

```toml
[project.optional-dependencies]
cpu = ["torch", "torchvision"]
cu130 = ["torch", "torchvision"]

[tool.uv]
conflicts = [
  [
    { extra = "cpu" },
    { extra = "cu130" },
  ],
]

[tool.uv.sources]
torch = [
  { index = "pytorch-cpu", extra = "cpu" },
  { index = "pytorch-cu130", extra = "cu130" },
]
torchvision = [
  { index = "pytorch-cpu", extra = "cpu" },
  { index = "pytorch-cu130", extra = "cu130" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
explicit = true
```

Replace versions and packages with confirmed project requirements. Declare every pair
of incompatible backend extras in `tool.uv.conflicts`. Set every PyTorch index to
`explicit = true` so unrelated packages continue to come from the default index.

Use environment markers instead of extras only when the backend is determined entirely
by platform, such as CUDA on Linux and CPU on macOS. Markers cannot distinguish two
Linux machines that require different CUDA builds.

ROCm and XPU builds may require matching Triton packages from the same explicit index.
Copy the exact dependency and marker pattern from the current upstream guide for the
selected backend; do not generalize a CUDA example.

## Quick Experiments Using uv pip

For a requirements-based quick experiment, `uv pip install ... --torch-backend=auto`
may detect the local CPU, CUDA, ROCm, or XPU backend. This is machine-local convenience,
not a reproducible cross-environment lock strategy. Record a specific
`--torch-backend=<backend>` command when repeatability matters.

`--torch-backend` is available only for the `uv pip` interface. Do not place it on
`uv add`, `uv lock`, or `uv sync` commands.

## Generated Harness

Record the supported environment matrix, extra selected by each setup/CI/container
command, driver or base-image assumptions, and the command used to verify
`torch.cuda`, ROCm, or XPU availability. Keep CPU CI as the default unless a dedicated
accelerator runner is part of the project contract.

## Source

- https://docs.astral.sh/uv/guides/integration/pytorch/
