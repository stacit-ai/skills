# .gitmessage Template for Conventional Commits

Copy this file to your repository root and configure git to use it:

```bash
cp .gitmessage ~/.gitmessage          # user-level (all repos)
git config commit.template .gitmessage  # project-level
# or
git config --global commit.template ~/.gitmessage  # global
```

---

## Template file content

Save the block below as `.gitmessage` in your project root (remove the code fence):

```
# <type>[(<scope>)][!]: <description>
#
# type (required) — choose one:
#   feat     new user-visible feature              → MINOR bump
#   fix      bug fix                               → PATCH bump
#   docs     documentation only
#   style    whitespace/formatting, no logic change
#   refactor code restructuring, no behavior change
#   perf     performance improvement               → PATCH bump
#   test     add or update tests
#   build    build system or dependency changes
#   ci       CI configuration changes
#   chore    maintenance (no src/test changes)
#   revert   revert a prior commit
#
# scope (optional) — noun describing the changed area: (auth), (api), (parser)
# !             — append before : to flag a breaking change
# description   — imperative mood, lowercase, no trailing period, ≤ 50 chars total
#
# ─────────────────────────────────────────────────────────────────────────────
# Blank line required between subject and body
# Body lines must be ≤ 72 characters
# Explain WHY, not HOW — the diff shows the implementation
# ─────────────────────────────────────────────────────────────────────────────
#
# Footer examples (one per line, after body):
#   BREAKING CHANGE: <what breaks and migration path>
#   Closes #<issue-number>
#   Co-authored-by: Name <email@example.com>
#   Reviewed-by: Name
#
# ─────────────────────────────────────────────────────────────────────────────
# Examples:
#
#   feat(auth): add OAuth2 login via GitHub
#
#   fix: prevent crash when config file is missing
#
#   feat!: require authentication on all API endpoints
#
#   BREAKING CHANGE: unauthenticated requests now return 401 instead of
#   returning partial data. Clients must include a Bearer token.
# ─────────────────────────────────────────────────────────────────────────────
```

## Customization Notes

- Replace the `type` list with your project's `commitlint` `type-enum` if it differs
- Add required scopes from `scope-enum` as a comment reference
- Remove footer examples that your project does not use
- Keep comments under 72 characters per line so they display cleanly in terminal editors
