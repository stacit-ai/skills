# QUALITY.md — Skill Quality Standards

## What Makes a Good Skill

A skill is good when an agent loading it produces correct, consistent output for the
intended task without additional guidance. Evaluate against that criterion, not against
documentation completeness.

## Content Requirements

**Ground in real artifacts, not training knowledge.**
Base content on: internal runbooks, API specs, code review comments, git diffs, incident
reports. Generic best-practice summaries are low-value — hard to distinguish from the
agent's baseline knowledge.

**Add what the agent lacks; omit what it knows.**
Include: project-specific conventions, non-obvious edge cases, exact tool names and
flags, sequencing constraints that would not be guessed. Exclude: general explanations
of standard concepts (HTTP, CSV, database migrations).

**Scope coherently.**
One skill = one coherent unit of work. Too narrow forces multi-skill loads and risks
conflicting instructions. Too broad makes trigger conditions unreliable.

**Calibrate specificity to fragility.**
Be prescriptive when an operation is fragile or must follow a specific sequence.
Give the agent freedom when multiple valid approaches exist — in those cases, explain
*why* rather than prescribing rigid steps.

**Target general, cross-framework, cross-system audiences.**
Skills in this repository are publicly released for any agent using any framework or
platform. Do not assume a specific language runtime, cloud provider, or proprietary
toolchain. If a skill genuinely requires a specific environment, state the restriction
explicitly in `docs/specs/<name>.md`.

**Document external dependencies in the spec, not the skill body.**
If a skill depends on an external API, library, component, or service, the spec file
(`docs/specs/<name>.md`) is the appropriate place to record its name, version
constraints, and access requirements. The SKILL.md body must remain self-contained —
it must not reference the spec file or any other file outside `skills/<name>/`.

## SKILL.md Structural Constraints

| Field | Rule |
|---|---|
| `name` | Lowercase `a-z`, digits `0-9`, hyphens only; max 64 chars; must match directory name |
| `description` | 1–1024 chars; imperative phrasing; covers indirect trigger phrasings |
| `compatibility` | ≤ 500 chars; include only when environment requirements exist |
| Body length | Under 500 lines and under 5,000 tokens |

The `description` is the only text an agent reads before deciding to activate the skill.
Cover indirect phrasings — not only the explicit domain name.

## Body Writing Rules

- Write step-by-step workflow instructions, not a feature list.
- Include a **Gotchas** section: domain-specific facts the agent would get wrong by
  reasonable assumption. Add or update gotchas only when a correction reveals a
  reusable, non-obvious failure mode. Do not add general advice ("handle errors
  appropriately").
- One default approach per task; mention alternatives in a single sentence. Do not
  present equal options — agents given menus make inconsistent choices.

## Resource Placement Rules

- Design the `SKILL.md` workflow first, then decide which supporting files are needed.
- Keep instructions needed on every run or most runs in `SKILL.md`.
- Move explanatory material to `references/` only when it is needed under a specific
  condition and is substantial enough to justify a separate load. Every reference file
  load instruction must specify *when* to load it, not just that the file exists.
- Use `assets/` only for fixed or semi-fixed material the agent will copy, apply, or
  lightly edit when writing into a project. Asset decisions depend on fixed content or
  stable structure, not length.
- Do not use assets for content that should vary substantially by task, audience, or
  user request. Use instructions instead, placed in `SKILL.md` or in conditional
  `references/` according to the same loading rules.
- Do not put decision rules, workflow steps, explanatory reference material, or
  one-off examples in `assets/`.

## Script Rules (Within Skills)

Scripts inside `skills/<name>/scripts/` must:

- Be Python (uv) or Deno only
- Include a shebang and inline dependency metadata
- Accept all input via CLI flags; no interactive prompts
- Output structured data (JSON preferred) to stdout; diagnostics to stderr
- Implement `--help`
- Use exit codes: 0 success, 1 error, 2 bad arguments

If a skill bundles scripts, the `SKILL.md` metadata must briefly note the required
runtime (`uv` or `deno`).

## Spec Files

Every `skills/<name>/` must have a corresponding `docs/specs/<name>.md`. Spec files
clarify the skill's goal and provide context useful during authoring or future
revisions — they are not a formal format requirement and have no mandatory section
headings or structure.

Common content: the skill's intended trigger conditions, scope boundaries, and any
external dependencies.

## Review Checklist

### Repo structure checks

*(Verified by contributors and CI — not applicable to deployed skills.)*

- [ ] `docs/specs/<name>.md` exists and matches skill intent
- [ ] `name` in frontmatter matches directory name exactly
- [ ] All referenced external APIs, libraries, or services are documented in
      `docs/specs/<name>.md`
- [ ] `uv run scripts/check_skill.py skills/<name>/` passes without errors

### Skill content checks

*(Verified by reviewers — these constraints must hold in the deployed skill.)*

- [ ] `description` uses imperative phrasing and covers indirect triggers
- [ ] `Gotchas` contains only non-obvious, domain-specific facts
- [ ] Every reference file load instruction specifies a precise condition
- [ ] Assets contain only fixed or stable-pattern material to copy, apply, or lightly
      edit; no decision rules, explanatory references, one-off examples, or content
      that should be generated flexibly
- [ ] All scripts implement `--help` and accept input via flags only
- [ ] Skill makes no assumption about framework, runtime, or platform (unless
      `docs/specs/<name>.md` explicitly restricts scope)
- [ ] `SKILL.md` body references no files outside `skills/<name>/` — no `docs/`,
      `scripts/`, `WORKFLOW.md`, `QUALITY.md`, spec files, or any repo-level path
- [ ] No internal business logic, proprietary specs, or confidential runbooks
      (see SECURITY.md — External Content)
- [ ] No credentials, PII, or verbatim proprietary content
