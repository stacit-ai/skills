# Package And Tool References

Load this file when creating dependency, tool, framework, or reference sections in the
generated project harness.

## Core Tools

- uv: https://docs.astral.sh/uv/llms.txt
- Ruff: https://docs.astral.sh/ruff/llms.txt
- ty: https://docs.astral.sh/ty/llms.txt
- pytest: https://docs.pytest.org/en/stable/
- just: https://just.systems/man/en/
- pre-commit: https://pre-commit.com/

## Configuration

- Pydantic Settings: https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/index.md
- Hydra: https://hydra.cc/docs/intro/

## ML Frameworks

- Lightning: https://lightning.ai/llms.txt
- PyTorch 2.12: https://docs.pytorch.org/docs/2.12/llms.txt
- PyTorch versioned docs pattern: https://docs.pytorch.org/docs/<version>/llms.txt

## Hugging Face

- Hub overview: https://huggingface.co/docs/hub/llms.txt
- huggingface_hub: https://huggingface.co/docs/huggingface_hub/llms.txt
- huggingface.js: https://huggingface.co/docs/huggingface.js/llms.txt
- Transformers: https://huggingface.co/docs/transformers/llms.txt
- Diffusers: https://huggingface.co/docs/diffusers/llms.txt
- Datasets: https://huggingface.co/docs/datasets/llms.txt
- Transformers.js: https://huggingface.co/docs/transformers.js/llms.txt
- Tokenizers: https://huggingface.co/docs/tokenizers/llms.txt
- timm: https://huggingface.co/docs/timm/llms.txt
- Kernels: https://huggingface.co/docs/kernels/llms.txt
- PEFT: https://huggingface.co/docs/peft/llms.txt
- Accelerate: https://huggingface.co/docs/accelerate/llms.txt
- Optimum: https://huggingface.co/docs/optimum/llms.txt
- TRL: https://huggingface.co/docs/trl/llms.txt
- OpenEnv: https://huggingface.co/docs/openenv/llms.txt
- Safetensors: https://huggingface.co/docs/safetensors/llms.txt
- bitsandbytes: https://huggingface.co/docs/bitsandbytes/llms.txt
- LightEval: https://huggingface.co/docs/lighteval/llms.txt

## Usage Rules

- Copy only references relevant to the generated project.
- Prefer `llms.txt` links when available because future agents can load concise,
  agent-oriented documentation.
- Do not browse every reference during scaffolding. Browse or copy a URL only when
  project requirements make that tool relevant.
- If the user pins a framework version, prefer the matching versioned documentation URL.
