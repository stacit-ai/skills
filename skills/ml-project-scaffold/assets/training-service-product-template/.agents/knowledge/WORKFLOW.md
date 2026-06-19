# WORKFLOW.md

## Setup

Use root commands for common checks. Each subproject may have its own setup details
after dependencies and serving framework are chosen.

## Training To Service Handoff

Training artifacts must carry enough metadata for the service to load and run them
consistently. When the artifact format is chosen, document the exact handoff contract in
`GOALS.md`.

## Integration Checks

Keep automatic integration checks cheap. Prefer tiny fixtures that verify preprocessing,
artifact metadata, and representative inference behavior. GPU, model-download, and
artifact-building checks are manual-only by default.

## Service Framework Selection

Do not introduce a serving framework until requirements make one appropriate. Once a
framework is selected, update `service/AGENTS.md`, `QUALITY.md`, and command recipes
with the concrete rules.
