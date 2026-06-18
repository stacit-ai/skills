---
name: ml-project-scaffold
description: >
  Scaffold machine learning projects with the right file structure, dependency
  strategy, command runner, and agent harness for the project's lifecycle. Use when
  initializing ML repos, training/evaluation workspaces, quick model experiments, or
  training-plus-inference projects; also use when the user asks to create uv, justfile,
  data, output, CI, pre-commit, or AGENTS.md conventions for an ML codebase.
---

# ML Project Scaffold

Use this skill to create the initial project structure and harness for a machine
learning codebase. The central decision is lifecycle class: quick experiment,
reproducible training/evaluation, or training-plus-service product.

## Workflow

1. Inspect the target directory if it exists: current files, package manifests, harness
   files, data directories, command runners, and CI.
2. Classify the project before creating files:
   - **Quick experiment**: proves an idea quickly; low maintainability and
     reproducibility requirements.
   - **Reproducible training/evaluation**: training or evaluation must be repeatable
     and maintainable, but it is not an unattended service.
   - **Training-plus-service product**: training/evaluation and serving live in one
     repo to keep versions consistent, with long-term service maintenance needs.
3. If classification is ambiguous and the wrong choice would create the wrong harness
   thickness, ask the user which lifecycle class applies. Otherwise choose the smallest
   class that satisfies the stated goal.
4. Read the branch reference:
   - Read [references/quick-experiment.md](references/quick-experiment.md) when the
     project is a quick experiment.
   - Read [references/reproducible-training.md](references/reproducible-training.md)
     when the project is a reproducible training/evaluation project.
   - Read [references/training-service-product.md](references/training-service-product.md)
     when the project combines training/evaluation with inference or service code.
   - Read [references/package-references.md](references/package-references.md) when
     creating or updating dependency, tool, framework, or external reference sections.
5. Initialize the Python project before copying assets. Use `uv init` for one-project
   repos, and run `uv init` inside each Python subproject for multi-project repos.
6. Copy the matching harness/tool asset directory, then merge or edit the copied files
   to fit the generated project metadata. Use:
   - [assets/quick-experiment-template](assets/quick-experiment-template)
   - [assets/reproducible-training-template](assets/reproducible-training-template)
   - [assets/training-service-product-template](assets/training-service-product-template)
7. Create only the project directories the work actually needs, such as `configs/`,
   `data/`, `notebooks/`, `outputs/`, package modules, workflow files, or `tests/`.
8. Write all lasting code, architecture, data, quality, command, and reference rules
   into the generated project's harness files. Future agents in the created project
   will not see this skill.
9. Remove copied files that do not apply. Do not leave irrelevant tool configs in the
   generated project.
10. Verify the result: command list works, harness pointers resolve, ignored output and
   data rules match the selected project class, and no service framework is introduced
   unless the user requested one.

## Defaults

- Use `justfile` as the command runner unless the existing project already has a
  different committed runner.
- Prefer `uv` for Python environment and dependency management.
- Use type annotations for readability and IDE help, but do not enable static type
  checking by default for ML framework code.
- Prefer early failure over defensive handling. Add defensive handling only for known
  dirty-data cases where one bad record should not waste an expensive pipeline.
- Keep tests focused. Add tests when they protect custom components or reduce future
  debugging scope; mark expensive training or smoke tests as manual-only.

## Gotchas

- **The generated project cannot rely on this skill.** If a rule matters after
  scaffolding, write it into the generated harness, usually `AGENTS.md` or
  `.agents/knowledge/`.
- **Harness thickness follows lifecycle.** A quick experiment should not inherit the
  heavier knowledge base and CI policy of a product project.
- **Asset templates are harness/tool bundles, not complete project structures.** Copy
  the matching template after `uv init`, then create only the files and directories the
  specific project needs.
- **Service framework is not a default.** In training-plus-service repos, create a
  service boundary and local harness, but choose FastAPI, BentoML, TorchServe, or
  another serving stack only when requirements justify it.
- **Data directories have different mutability rules.** `data/raw` or `data/` is for
  raw immutable inputs; generated intermediates and products belong outside raw data.
- **Workflow entry files are entrypoints.** Do not design root workflow files as modules
  to import from elsewhere; shared logic belongs in the package.
