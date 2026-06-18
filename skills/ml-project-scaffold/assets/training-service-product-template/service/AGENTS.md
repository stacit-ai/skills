# AGENTS.md

## Project Shape

This subproject owns inference or service code. It intentionally starts
framework-neutral. Do not add FastAPI, BentoML, TorchServe, a queue worker, or another
serving framework until requirements justify the choice.

## Structure

- `src/` stores service code after the serving approach is selected.
- `tests/` stores service-local tests.
- Root `tests/integration/` stores train/service consistency tests.

## Rules

- Update this file when a service framework is chosen.
- Document request/response contracts, configuration, error handling, observability,
  deployment, and model artifact loading rules here.
- Keep training artifact compatibility aligned with root `.agents/knowledge/GOALS.md`.
- Service code should be maintained with product-level robustness; do not copy the
  lower robustness expectations of training scripts into service runtime code.
