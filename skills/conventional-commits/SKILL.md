---
name: conventional-commits
description: >
  Drafts git commit messages following the Conventional Commits 1.0.0 specification.
  Use when creating commit messages with a type prefix, when a project uses conventional
  commits, commitlint, or semantic-release, or when the user says "write a feat/fix
  commit", "use conventional commits", "CC format", "what type should I use", or when
  git history shows type-prefixed messages like "feat:", "fix:", "chore:".
---

# Conventional Commits

## Step 1 — Check Project Settings

Before drafting, read in this order:

1. `commitlint.config.*` or `.commitlintrc*` for:
   - `rules['type-enum']` — overrides the allowed type list below
   - `rules['scope-empty']` / `rules['scope-enum']` — determines scope requirements
   - Any other rules that modify format
2. `package.json` → `commitlint` key
3. `git log --oneline -20` — infer type casing, scope usage pattern, footer conventions

Hard rules from config and project history override all generic guidance in this skill.

## Step 2 — Select Format

**Short format** (title only): default. Use when:
- The title alone captures what changed and why
- The change is a single, self-evident operation (dependency bump, typo fix, config
  change, test addition)
- No notable trade-offs, side effects, or non-obvious motivation

**Long format** (title + blank line + body): use when:
- The reason is not obvious from the diff
- There are trade-offs, limitations, migration steps, or side effects to document
- The change fixes a bug whose root cause needs explanation
- The user explicitly requests a body

## Step 3 — Choose Type

Use this decision tree. Stop at the first matching rule.

```
Is this reverting a prior commit?
  YES → revert

Is this a build system or dependency change
      (webpack, gradle, package.json deps, etc.)?
  YES → build

Is this a CI pipeline change
      (.github/workflows, Jenkinsfile, .travis.yml, etc.)?
  YES → ci

Is there a user-visible behavior change that did not exist before?
  YES → Is it correcting incorrect behavior?
         YES → fix
         NO  → feat

Is this a code change with no external behavior change?
  YES → Does it produce a measurable performance improvement?
         YES → perf
         NO  → Is it restructuring or renaming without logic change?
                YES → refactor
                NO  → Is it cosmetic only (whitespace, formatting, lint rules)?
                       YES → style

Is this adding or updating tests only?
  YES → test

Is this updating documentation only?
  YES → docs

Everything else (release scripts, .gitignore, tooling not in build/ci):
  → chore
```

If the project's config defines a different `type-enum`, replace this tree with those
types.

## Step 4 — Determine Scope

**Default: omit scope.** Add scope only when:

1. The config requires it (`scope-empty: [2, "never"]`)
2. The last 20 commits consistently include scope for this kind of change
3. The user explicitly requests a scope

When using scope, match the granularity and naming found in project history. Do not
introduce a new scope convention if none is established.

Scope goes in parentheses immediately after the type: `feat(auth): ...`

## Step 5 — Handle Breaking Changes

A breaking change is any modification to a public interface that requires consumers to
update their code.

Two equivalent notations — use whichever appears in project history:

1. **`!` suffix** (concise, no explanation needed in footer):
   `feat!: remove deprecated login endpoint`

2. **`BREAKING CHANGE:` footer** (adds context alongside `!`):
   ```
   feat!: remove deprecated login endpoint

   BREAKING CHANGE: /api/v1/login has been removed. Use /api/v2/auth instead.
   ```

Both forms must be present together when a description is needed. Either form alone is
valid when no description is needed (use `!` then).

## Step 6 — Compose the Message

**Short format:**
```
<type>[(<scope>)][!]: <description>
```

**Long format:**
```
<type>[(<scope>)][!]: <description>

<body>

[BREAKING CHANGE: <explanation>]
[Closes #<issue>]
[Co-authored-by: Name <email@example.com>]
```

Rules:
- `<description>`: imperative mood, lowercase first letter, no trailing period
- One space after the colon: `fix: ` not `fix:  `
- Title ≤ 50 characters total (including type, scope, colon, space)
- Blank line between title and body
- Body lines ≤ 72 characters
- Each footer on its own line; footer tokens use `-` as word separator
  (`Reviewed-by:`, `Co-authored-by:`)
- `BREAKING CHANGE` is the only footer token that uses a space instead of `-`

## Step 7 — Validate

Validate the message manually using the checklist below, or use the project's own
commit-message linting or hook workflow if one is configured:

- [ ] Title ≤ 50 characters
- [ ] Title does not end with a period
- [ ] Blank line between title and body (if body present)
- [ ] Body lines ≤ 72 characters
- [ ] Type is in the project's allowed list

## Gotchas

- **`style` is cosmetic only** — whitespace, formatting, missing semicolons with no
  logic change. If a lint rule enforcement also alters logic, use `fix`.
- **`chore` is not a catch-all** — use it only for maintenance that touches no `src/`
  or test files. Adding a tool or config that affects the build is `build`.
- **`feat` requires net-new user-visible behavior** — extending an endpoint with a new
  optional parameter is `feat`; adding a required parameter is `feat!` (breaking).
- **Scope parentheses are literal `()`** — if history uses `[scope]` or `scope/`,
  match history; the spec mandates `()` but project convention takes precedence.
- **`BREAKING CHANGE` footer token is case-sensitive** — `breaking change:` is not
  recognized by semantic-release and most commitlint rules.
- **`revert` format** — include SHA and original subject:
  `revert: feat(auth): add OAuth2 support` with body `Reverts commit abc1234.`
- **Title length includes the type prefix** — `feat(authentication-service): ` is
  already 30 characters before the description begins.

## References

- Read [references/cc-spec.md](references/cc-spec.md) for the complete specification
  grammar, all format rules, and extended examples.
- Load [assets/gitmessage_template.md](assets/gitmessage_template.md) when the user
  asks to create or update a `.gitmessage` file for their project.
