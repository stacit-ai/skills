# GOALS.md

## Product Goal

Keep model training, evaluation, and inference behavior consistent across one versioned
repo while allowing training and service code to evolve with different local concerns.

## Shared Contracts

Document the chosen contracts here as the project matures:

- model artifact format
- preprocessing and postprocessing behavior
- tokenizer or feature schema
- config and metadata handoff
- representative inference fixtures
- compatibility expectations between training outputs and service inputs
