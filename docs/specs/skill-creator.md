# Spec: skill-creator

## Purpose

Guides an agent through building a well-structured, high-quality agent skill — covering
both spec compliance and the practices that make a skill effective in production.

The skill serves two mutually reinforcing roles:

1. **Context provision** — supplies spec rules, workflow steps, and instruction patterns
   the agent cannot reliably produce from training knowledge alone.
2. **Output restriction** — constrains agent output via gotchas and a concrete workflow,
   reducing variance in skill quality across runs.

## Trigger Conditions

**Explicit:**
- "create a skill for X"
- "scaffold a skill"
- "write a skill"
- "build a new skill"
- "make a skill"
- "fix this skill"
- "clean up this skill"
- "refactor this skill"
- "update the skill description"
- "add a gotcha to the skill"
- "add a script to the skill"

**Indirect (must also trigger):**
- "I want agents to do X automatically"
- "package this workflow as a skill"
- "how do I teach the agent to do X"
- "help me document this workflow for agents"
- "the agent keeps doing X wrong — I want to fix it"

## What the Agent Lacks

Without this skill, an agent would likely:

- Write skill content for humans (verbose, polite) rather than for agents (concise,
  directive), wasting context budget
- Add too many options instead of one default with a brief alternative, causing
  inconsistent downstream choices
- Write general advice in Gotchas ("handle errors appropriately") instead of
  domain-specific, non-obvious facts
- Create empty optional subdirectories (`scripts/`, `references/`, `assets/`)
  preemptively
- Use non-compliant names (uppercase, underscores, spaces, consecutive hyphens)
- Write a `description` that covers only the explicit domain name, missing indirect
  trigger phrasings
- Load reference files unconditionally, defeating progressive disclosure
- Split reference files by sub-topic rather than by branching condition, causing
  either all files to load simultaneously (defeating progressive disclosure) or files
  that can never be assigned a clean when-to-load trigger
- Move content to reference files before designing the `SKILL.md` workflow, producing
  references that do not correspond to real conditional branches
- Move content that is needed on most runs, or branch content too small to justify a
  separate load, into reference files and defeat progressive loading instead of
  preserving it
- Write templates that over-constrain output by specifying content rather than structure
- Move non-fixed, task-dependent output into assets, causing generated work to follow
  a template when it should remain flexible
- Put explanatory guidance or decision rules in assets instead of SKILL.md or
  conditional references
- Embed repo-internal steps in the generated `SKILL.md` body — for example, "create
  `docs/specs/<name>.md` first" or "run `validate_harness.py`" — making the skill
  unusable when deployed outside this repository where those files do not exist

## Scope

One coherent work unit: creating or modifying a single skill from definition through
a working first draft. Scope includes:

- Planning the skill's purpose, trigger conditions, and necessary content
- Writing `SKILL.md` (frontmatter + body)
- Adding scripts, references, and assets within the skill directory
- Reviewing output against the spec

Out of scope:

- Designing the skill's domain content — the agent is a facilitator; domain knowledge
  must come from the user or external artifacts, not from LLM training knowledge
- Managing multiple skills simultaneously
- Tooling, CI, or repo infrastructure decisions in the consuming project
- Referencing repo-internal files (`docs/specs/`, `WORKFLOW.md`, `QUALITY.md`,
  `scripts/validate_harness.py`) in the generated `SKILL.md` body — the skill must
  be deployable standalone in any project that does not contain this repository

## Content Boundaries

**Include in `SKILL.md` body (loaded on every invocation):**
- Core principles that shape how the agent writes all skill content
- Workflow steps covering the full creation process
- Gotchas — the highest-value content, derived from known failure modes only
- Instruction patterns and guidance on when to use each type
- Content needed on every run or most runs, even when it belongs to a recognizable
  topic

**Never include in `SKILL.md` body:**
- References to files outside `skills/<name>/` — no `docs/specs/`, `WORKFLOW.md`,
  `QUALITY.md`, `scripts/validate_harness.py`, or any other repo-level path.
  End users deploy only the skill directory; those files do not exist in their context.

**Move to `references/` (loaded on demand):**
- Hard spec constraint tables (frontmatter field rules, name character rules, body
  limits) — needed only when validating or uncertain about a constraint
- Explanatory guidance that is needed only after the `SKILL.md` workflow enters a
  specific condition branch and is substantial enough to justify a separate load.
  Design the SKILL.md workflow first, then split references only where that workflow
  exposes real load conditions.

**Move to `assets/` (loaded on demand):**
- Fixed or semi-fixed material the agent should copy, apply, or lightly edit when
  writing into a project
- Templates whose output structure is intentionally stable, with only small fields or
  sections to change
- Reusable static resources. Asset decisions depend on fixed content or stable
  structure, not length. Non-fixed output guidance belongs as instructions in
  `SKILL.md` or in conditional `references/`, not as an asset.

## Gotchas Source

All gotchas in `SKILL.md` must come from confirmed failure modes, not generic advice.

1. Name in frontmatter not matching parent directory name → spec validation fails
2. Empty optional subdirectories created preemptively → misleads agents about available
   resources
3. Reference load instructions without precise conditions → agent loads all files on
   every run, defeating progressive disclosure
4. Templates that include sample content (not just structural boilerplate) → agent
   produces variants of the template instead of generating appropriate content
5. `description` covering only explicit domain name → skill fails to activate on valid
   indirect use cases
6. General advice in Gotchas ("validate inputs") → wastes tokens, no signal value
7. Multiple equal options presented → inconsistent tool/approach selection across runs
8. Embedding repo-internal steps in generated `SKILL.md` (e.g. "create
   `docs/specs/<name>.md`", "run `validate_harness.py`") → skill becomes unusable
   when deployed outside this repository where those files and scripts do not exist
9. Reference files split by topic instead of branching condition → files are either
   always loaded together (same effect as putting content in SKILL.md) or cannot be
   assigned a single clean when-to-load condition; each file must correspond to
   exactly one decision branch
10. Reference files created before the SKILL.md workflow is designed → files do not
    match real branch points and get loaded too broadly
11. Frequently needed or tiny branch content moved to `references/` → files load too
    broadly or cost more than progressive disclosure saves
12. Non-fixed content moved to `assets/` → generated output is constrained by a
    template when it should vary by task
13. Explanatory guidance placed in `assets/` → agents treat guidance as copyable
    material instead of instructions

## Quality Bar

A skill produced with this skill passes if:

- `name` in frontmatter matches the directory name exactly
- `description` uses imperative phrasing and covers at least three indirect trigger
  phrasings the user might say without naming the domain
- Every reference file load instruction specifies a precise trigger condition
- `SKILL.md` body is under 500 lines
- An agent loading the resulting skill produces correct output for the target task on
  the first attempt without additional user guidance
