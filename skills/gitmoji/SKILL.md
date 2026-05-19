---
name: gitmoji
description: >
  Drafts git commit messages following the gitmoji specification: selects the correct
  emoji for the change intent and composes a structured message. Use when creating
  emoji-prefixed commit messages, when a project uses gitmoji, or when the user says
  "use gitmoji", "what emoji for this commit", "gitmoji format", or when git history
  shows messages that begin with an emoji or an emoji code like ":bug:".
---

# Gitmoji

## Step 1 — Check Project Conventions

Before drafting:

1. Run `git log --oneline -10` to determine:
   - **Emoji format**: unicode character (`🐛`) or text code (`:bug:`) — match what
     history uses; default to unicode if history is absent
   - **Scope usage**: parentheses `(scope)` — only if history uses it
   - **Description style**: standalone emoji title vs. combined emoji + CC-style type

2. Check `CONTRIBUTING.md` or `AGENTS.md` for any gitmoji-specific rules

Project history overrides generic guidance.

## Step 2 — Select Emoji

Use the decision guide below. Load
[references/gitmoji-reference.md](references/gitmoji-reference.md) when the right
emoji is not immediately clear or when multiple candidates exist.

**Quick selection guide by intent:**

| Intent | Emoji | Code |
|---|---|---|
| New feature | ✨ | `:sparkles:` |
| Bug fix | 🐛 | `:bug:` |
| Critical hotfix | 🚑️ | `:ambulance:` |
| Performance improvement | ⚡️ | `:zap:` |
| Refactor (no behavior change) | ♻️ | `:recycle:` |
| Remove code or files | 🔥 | `:fire:` |
| Documentation | 📝 | `:memo:` |
| Add or update tests | ✅ | `:white_check_mark:` |
| Fix a failing test | 🧪 | `:test_tube:` |
| Upgrade dependency | ⬆️ | `:arrow_up:` |
| Downgrade dependency | ⬇️ | `:arrow_down:` |
| Fix CI build | 💚 | `:green_heart:` |
| Add or update CI | 👷 | `:construction_worker:` |
| Fix security or privacy issue | 🔒️ | `:lock:` |
| Breaking change | 💥 | `:boom:` |
| Work in progress | 🚧 | `:construction:` |
| Revert changes | ⏪️ | `:rewind:` |
| Merge branches | 🔀 | `:twisted_rightwards_arrows:` |
| Release / version tag | 🔖 | `:bookmark:` |
| Fix linter warnings | 🚨 | `:rotating_light:` |
| Move or rename resources | 🚚 | `:truck:` |
| Improve structure / format | 🎨 | `:art:` |
| Add or update configuration | 🔧 | `:wrench:` |
| Add or update dev scripts | 🔨 | `:hammer:` |
| Fix typo | ✏️ | `:pencil2:` |
| Add or update dependencies (add) | ➕ | `:heavy_plus_sign:` |
| Remove a dependency | ➖ | `:heavy_minus_sign:` |
| Begin a project | 🎉 | `:tada:` |
| Deploy | 🚀 | `:rocket:` |
| Internationalization | 🌐 | `:globe_with_meridians:` |

When two emojis seem equally valid, prefer the more specific one (`🐛` over `🔧` for a
bug fix even if configuration was touched).

## Step 3 — Select Format

**Short format** (emoji + description): default. Use when:
- The intent is self-evident from the emoji and a brief title
- No trade-offs, non-obvious motivation, or migration notes

**Long format** (emoji + description + blank line + body): use when:
- The reason for the change is not obvious from the diff
- There are trade-offs, limitations, or side effects worth documenting
- The change is a breaking change that needs migration guidance

## Step 4 — Compose the Message

**Short format:**
```
<emoji> [(<scope>)]: <description>
```

**Long format:**
```
<emoji> [(<scope>)][!]: <description>

<body — explain why, not how>

[BREAKING CHANGE: <explanation>]
[Closes #<issue>]
```

Rules:
- One emoji per commit message (the primary intent)
- `<description>`: imperative mood, lowercase first letter, no trailing period
- Title (emoji + scope + description) ≤ 50 characters total
- Blank line between title and body
- Body lines ≤ 72 characters
- Use `!` after the emoji (before `:`) and a `BREAKING CHANGE:` footer for breaking
  changes: `💥!: remove legacy API endpoints`

**Emoji format:** match the project's history. When no history exists, use the unicode
character directly (e.g., `✨`) rather than the text code (`:sparkles:`).

## Step 5 — Validate

Verify:

- [ ] Emoji is the first character of the title
- [ ] Title ≤ 50 characters (emoji counts as 1–2 characters)
- [ ] Title does not end with a period
- [ ] Blank line between title and body (if body present)
- [ ] Body lines ≤ 72 characters
- [ ] Emoji matches the primary intent of the change

## Gotchas

- **One emoji per message** — using multiple emojis (e.g., `✨🐛`) is not standard
  gitmoji. If a commit genuinely fixes a bug while also adding a feature, consider
  splitting the commit; otherwise use the emoji for the dominant intent.
- **`🚧` is not for unfinished experiments** — use it for deliberate WIP commits that
  will be continued. Speculative or throwaway code should not be committed at all.
- **`🔥` removes; `🗑️` deprecates** — `🔥 (:fire:)` is for outright deletion; `🗑️
  (:wastebasket:)` marks code as deprecated pending removal in a future commit.
- **`⚡️` is performance, not "fast feature"** — use only when the commit's primary
  purpose is a measurable speed or memory improvement.
- **`💥` is reserved for breaking changes** — it should appear alongside `!` and a
  `BREAKING CHANGE:` footer. Do not use it for dramatic but non-breaking refactors.
- **Text code vs unicode** — some terminals and tools do not render unicode emoji; some
  git GUIs do not render text codes. Match the project's existing format.
- **Emoji character width** — terminals render most emoji as double-width (2 columns).
  This affects visual alignment but not the 50-character title rule, which counts
  codepoints.

## References

- Load [references/gitmoji-reference.md](references/gitmoji-reference.md) when
  selecting an emoji and the quick guide above does not contain a clear match.
