---
name: skill-creator
description: >
  Build and improve Agent Skills following spec-compliant structure and effective
  instruction patterns. Use when asked to create, scaffold, refactor, or fix a
  skill — including writing descriptions, adding scripts, organizing reference
  files, or updating gotchas — even if the user just says "make a skill for X",
  "write a skill", or "clean up this skill".
---

# Skill Creator

Agent skills serve one of two roles — or both:

- **Context provision**: supplies knowledge the agent lacks (project-specific
  conventions, domain procedures, non-obvious edge cases, exact APIs)
- **Output restriction**: reduces output variance via gotchas, templates, and
  checklists to raise quality

## Core Principles

- **Add what agent lacks; omit what it knows.** Project-specific conventions,
  non-obvious edge cases, exact APIs to use. Skip explanations of standard concepts.
- **Scope = one coherent work unit.** Too narrow → conflicting instructions from
  multi-skill loads. Too broad → unreliable triggers.
- **Calibrate specificity to fragility.** Fragile or ordered operations → prescriptive
  steps. Multiple valid approaches → explain why, not what.
- **Teach the approach, not the instance.** Instructions generalize across task
  variations even when individual details differ.
- **One default per decision.** Alternatives in one sentence. Never present equal
  options — agents make inconsistent choices.
- **Write for agents, not humans.** Concise, directive. No pleasantries.

## Instruction Patterns

Not every skill needs all of these. Use them when they apply.

**Gotchas** — Highest value. Non-obvious facts the agent would get wrong by reasonable
assumption: naming inconsistencies, soft deletes, endpoints that lie, required flags
that aren't obvious. Add a new gotcha on every correction. Domain-specific facts only —
no general advice ("validate inputs").

**Templates** — Structure only, not content. Invariant boilerplate (a language's
shebang + metadata header, a fixed output format) is safe to template; task-specific
logic is not. Short templates inline; longer or conditional ones in `assets/`. Templates
that specify content constrain output diversity — use them only for truly fixed parts.

**Checklists** — For multi-step workflows with dependencies or validation gates.

**Validation loops** — Do → validate → fix → repeat. A script that produces clear errors
("Field 'x' missing — available: a, b, c") enables self-correction without a round-trip.

**Plan-validate-execute** — For batch or destructive operations: produce a structured
plan file, validate against a source of truth, then execute. Never skip validation.

**Script bundling** — Extract to `scripts/` when the same logic would be regenerated
identically every invocation (validators, parsers, formatters). Generate inline when
logic is one-off or varies significantly by task.

## Workflow

### 1. Define the Skill

Before creating any files, answer:

- What task does this skill cover?
- When should it trigger — including indirect phrasings the user might say without
  naming the domain?
- What does the agent lack that makes this skill necessary? If the agent handles the
  task well without it, the skill adds no value.
- Is this one coherent work unit, or should it be split?

### 2. Plan the Structure

```
skill-name/
├── SKILL.md           ← required
├── scripts/           ← only if executable logic is needed
├── references/        ← only if detailed reference material is needed
└── assets/            ← only if templates or static resources are needed
```

Create subdirectories only when at least one file will go in them.

Name rules: lowercase `a-z`, digits `0-9`, hyphens only; no leading/trailing/consecutive
hyphens; max 64 characters.

### 3. Write `SKILL.md`

Load [assets/skill_template.md](assets/skill_template.md) for frontmatter boilerplate.

Frontmatter checklist:

- [ ] `name` matches the directory name exactly
- [ ] `description`: First sentence in third person = capability statement (action
  verbs + domain keywords; no internal implementation details). Remaining sentences:
  imperative "Use when…" focused on user intent and task — not internal components
  (scripts, templates, output format). Cover indirect phrasings a user might say
  without naming the domain. 1–1024 chars.
  - **Good**: "Extract text and tables from PDF files, fill forms, and merge
    documents. Use when working with PDF files or when the user mentions PDFs,
    forms, or document extraction."
  - **Bad**: "Helps with documents." — agent cannot distinguish this skill from
    any other document-related skill.
- [ ] `compatibility` ≤ 500 chars (include only if specific environment is required)
- [ ] Remove `allowed-tools` and `metadata` unless intentionally needed

Body checklist:

- [ ] Workflow steps (action-oriented verbs, not a feature list)
- [ ] Gotchas section (domain-specific non-obvious facts only)
- [ ] Every reference file load instruction specifies a precise trigger condition
- [ ] Under 500 lines

### 4. Add Scripts (if needed)

Add a script when any of these conditions holds:
- The operation is deterministic and would produce identical code on every invocation.
- Without the script, the same logic must be regenerated from scratch each time.
- Errors require structured, explicit output that inline code generation cannot
  reliably provide.

Generate inline first. Extract to a script only after the pattern repeats across
multiple runs.

Load the language-specific reference and template before writing:

- Python (uv): read [references/python_script_spec.md](references/python_script_spec.md),
  load [assets/uv_script_template.py](assets/uv_script_template.py)
- Deno: read [references/deno_script_spec.md](references/deno_script_spec.md),
  load [assets/deno_script_template.ts](assets/deno_script_template.ts)
- Bun: read [references/bun_script_spec.md](references/bun_script_spec.md),
  load [assets/bun_script_template.ts](assets/bun_script_template.ts)
- Ruby: read [references/ruby_script_spec.md](references/ruby_script_spec.md),
  load [assets/ruby_script_template.rb](assets/ruby_script_template.rb)

Every script in `scripts/` must be introduced in `SKILL.md` with a markdown relative
link at its **first mention**, before any invocation example:

```markdown
Use [`scripts/validate.py`](scripts/validate.py) to check the output format.
```

This signals to the agent that the path is relative to the skill directory root, not
the consuming project's root. Without the link, `scripts/foo.py` in a code block is
ambiguous.

All scripts must follow these rules regardless of language:

- **No interactive prompts** — agents run in non-interactive shells; TTY prompts hang
  indefinitely. Accept all input via flags.
- **`--help` output** — the primary interface discovery mechanism for agents.
- **Data to stdout, diagnostics to stderr** — structured output (JSON preferred)
  enables downstream composability.
- **Meaningful exit codes** — 0 success, 2 bad arguments, 1 general error; document
  any non-standard codes in `--help`.
- **Idempotent by default** — agents may retry; "create if absent" is safer than
  "fail on duplicate".
- **Meaningful output** — errors must state what is wrong, why, and how to fix it;
  a linter that only reports the offending line without explanation forces a
  round-trip back to the agent.

### 5. Add References and Assets (if needed)

Reference files go in `references/`. One topic per file.

In `SKILL.md`, every load instruction must specify a precise trigger condition:

```markdown
- Read [references/api-errors.md](references/api-errors.md) if the API returns a non-200 status.
```

Not: "See references/ for details" — the agent needs to know *when* to load each file.

Asset templates go in `assets/`. Structural boilerplate only — no implementation logic
or sample content that would constrain the agent's output.

### 6. Review Against the Spec

If the skill has a `scripts/` directory, run the bundled validators and resolve all
errors before proceeding; review warnings:

- [scripts/check_metadata.py](scripts/check_metadata.py) — validates frontmatter
  fields and body line count; accepts `--skill PATH` and `--json`
- [scripts/check_structure.py](scripts/check_structure.py) — validates directory
  structure and script file types; accepts `--skill PATH` and `--json`

Manual checks (always required — cover semantics the scripts cannot verify):

- [ ] `description` is in third person and covers indirect trigger phrasings
- [ ] All file references use relative paths from the skill root
- [ ] No reference file loaded without a precise trigger condition
- [ ] `name` matches directory name exactly
- [ ] `compatibility` ≤ 500 chars (if present)
- [ ] Body under 500 lines

Load [references/spec_hard_rules.md](references/spec_hard_rules.md) if any check result is unclear.

## Gotchas

- **`name` must exactly match the parent directory name** — mismatch fails spec
  validation; frontmatter is the authoritative source
- **Don't create empty subdirectories** — preemptive `scripts/`, `references/`,
  `assets/` mislead agents into expecting files that don't exist
- **Reference load instructions require precise trigger conditions** — "when X" not
  "see references/"; without a condition the agent loads everything every run
- **Script templates must be structural boilerplate only** — including implementation
  logic causes agents to produce template variants; only shebang, metadata block,
  arg-parsing scaffold, and I/O routing are invariant
- **`description` is the only text read before activation** — must cover indirect
  phrasings or the skill won't trigger on valid use cases
- **Gotchas are for domain-specific non-obvious facts only** — general advice
  ("handle errors", "validate inputs") adds no signal and wastes context

## References

- Read [references/spec_hard_rules.md](references/spec_hard_rules.md) when validating
  frontmatter or uncertain about a constraint.
- Read [references/python_script_spec.md](references/python_script_spec.md) when
  adding a Python (uv) script.
- Read [references/deno_script_spec.md](references/deno_script_spec.md) when adding
  a Deno script.
- Read [references/bun_script_spec.md](references/bun_script_spec.md) when adding
  a Bun script.
- Read [references/ruby_script_spec.md](references/ruby_script_spec.md) when adding
  a Ruby script.
- Use the `skills-spec` MCP server (`httpUrl: https://agentskills.io/mcp`) to query
  official spec rules and field constraints.
