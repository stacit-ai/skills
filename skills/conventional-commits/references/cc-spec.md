# Conventional Commits 1.0.0 — Specification Reference

Source: https://www.conventionalcommits.org/en/v1.0.0/

## Summary

The Conventional Commits specification defines a lightweight convention on top of
commit messages that provides an explicit commit history making it easy to write
automated tools on top of.

## Message Structure

```
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

## Specification Rules

1. Commits MUST be prefixed with a type, which consists of a noun (`feat`, `fix`, etc.),
   followed by the optional scope, optional `!`, and a required colon and space.
2. The type `feat` MUST be used when a commit adds a new feature to the application or
   library.
3. The type `fix` MUST be used when a commit represents a bug fix for the application.
4. A scope MAY be provided after a type. A scope MUST consist of a noun describing a
   section of the codebase surrounded by parentheses, e.g., `fix(parser):`.
5. A description MUST immediately follow the colon and space after the type/scope
   prefix. The description is a short summary of the code changes.
6. A longer commit body MAY be provided after the short description, providing
   additional contextual information about the code changes. The body MUST begin one
   blank line after the description.
7. A commit body is free-form and MAY consist of any number of newline separated
   paragraphs.
8. One or more footers MAY be provided one blank line after the body. Each footer MUST
   consist of a word token, followed by either `:<space>` or `<space>#` separator,
   followed by a string value.
9. A footer's token MUST use `-` in place of whitespace characters (e.g.,
   `Acked-by`). `BREAKING CHANGE` is an exception and MAY also be used as a token.
10. A footer's value MAY contain spaces and newlines, and parsing MUST terminate when
    the next valid footer token/separator pair is observed.
11. Breaking changes MUST be indicated in the footer portion of a commit, by including
    the text `BREAKING CHANGE:`, or appending a `!` after the type/scope. When used as
    a token, a breaking change MUST include uppercase text `BREAKING CHANGE`, followed
    by a colon, space, and description.
12. If included as a footer, a breaking change MUST consist of the uppercase text
    `BREAKING CHANGE`, followed by a colon, space, and description.
    e.g., `BREAKING CHANGE: environment variables now take precedence over config files`.
13. `!` MAY be appended prior to the `:` in the type/scope prefix, to further draw
    attention to breaking changes. `BREAKING CHANGE: description` MUST also be
    included in the footer section if `!` is used.
14. Types other than `feat` and `fix` MAY be used in commit messages.
15. The units of information that make up Conventional Commits MUST NOT be treated as
    case sensitive by implementors, with the exception of `BREAKING CHANGE` which MUST
    be uppercase.
16. `BREAKING-CHANGE` MUST be synonymous with `BREAKING CHANGE` when used as a token
    in a footer.

## Standard Types

| Type | Semver bump | When to use |
|---|---|---|
| `feat` | MINOR | New user-visible feature |
| `fix` | PATCH | Bug fix |
| `docs` | — | Documentation only |
| `style` | — | Whitespace, formatting, no logic change |
| `refactor` | — | Code restructuring, no behavior change |
| `perf` | PATCH | Performance improvement |
| `test` | — | Add or update tests |
| `build` | — | Build system or dependency changes |
| `ci` | — | CI configuration changes |
| `chore` | — | Other maintenance (no src/test changes) |
| `revert` | varies | Revert a prior commit |

Breaking changes (`BREAKING CHANGE` footer or `!`) → MAJOR bump regardless of type.

## Format Examples

### Short format — bug fix
```
fix(auth): reject expired JWT tokens
```

### Short format — new feature
```
feat: add dark mode toggle to settings
```

### Long format — feature with context
```
feat(api): add rate limiting to all endpoints

Without rate limiting, a single client can exhaust the connection pool
under sustained load. This change adds a sliding-window limiter (100
req/min per IP) using Redis. The limit is configurable via
RATE_LIMIT_MAX env var.
```

### Breaking change with `!` and footer
```
feat!: replace session cookies with JWT

BREAKING CHANGE: all existing sessions are invalidated on upgrade.
Users must re-authenticate. The Set-Cookie header is no longer issued.
```

### Breaking change — API removal
```
refactor!: drop support for Node.js 16

BREAKING CHANGE: Node.js 16 reached end-of-life. The minimum supported
version is now Node.js 20.
```

### Revert
```
revert: feat(auth): add OAuth2 provider support

Reverts commit 3a4b5c6. OAuth2 integration introduced a regression in
the password reset flow that is not yet fixed.
```

### Multiple footers
```
fix(deps): upgrade axios to 1.7.2

Fixes a SSRF vulnerability in redirect handling (CVE-2024-XXXXX).

Closes #482
Reviewed-by: Jane Doe
```

## Footer Token Rules

- Word token + `: ` or ` #` separator + value
- `-` replaces spaces in token names: `Co-authored-by:`, `Reviewed-by:`
- `BREAKING CHANGE` is the only token that uses a space (not a hyphen)
- Multiple footers: each on its own line

## Grammar (ABNF)

```
commit           = title LF LF body LF LF footers
                 / title LF LF body
                 / title LF LF footers
                 / title
title            = type [scope] ["!"] ":" SP description
type             = 1*wchar
scope            = "(" *wchar ")"
description      = 1*(wchar / SP)
body             = paragraph *(LF paragraph)
paragraph        = 1*(wchar / SP / LF)
footers          = footer *(LF footer)
footer           = token ": " value
                 / token " #" value
token            = "BREAKING CHANGE"
                 / 1*(wchar / "-")
value            = 1*(wchar / SP / LF)
wchar            = %x21-7E / %x80-10FFFF   ; any non-space, non-control char
```

## Semver Correlation

| Commit type | Version bump |
|---|---|
| `fix` | PATCH |
| `feat` | MINOR |
| `BREAKING CHANGE` or `!` | MAJOR |
| All others | No bump (or PATCH, tooling-dependent) |
