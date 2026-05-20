# Thick Harness Component Specifications

Reference for projects classified as **Thick (Long-term Maintainable)**. Load when
the project requires full-suite harness components.

---

## AGENTS.md — Structural Rules

**Canonical section order:**

1. Project name + one-line description
2. Annotated directory tree (max depth 2; omit generated or dependency directories)
3. Core conventions (language, style, naming — bullet points; defer details to KB)
4. When-to-read-what table (document path → specific trigger condition)
5. Validation commands (if applicable)

**Line budget per section:**

| Section | Target | Hard limit |
|---|---|---|
| Name + description | 3 | 5 |
| Directory tree | 15 | 25 |
| Core conventions | 15 | 25 |
| When-to-read-what table | 10 | 20 |
| Validation | 5 | 10 |
| **Total** | **≤ 100** | **≤ 150** |

**Enforcement rules:**
- Any instruction longer than one sentence belongs in a KB file or skill, not AGENTS.md.
- Duplication between AGENTS.md and KB/skills is a defect; remove the AGENTS.md copy.
- The when-to-read-what table is the primary navigation mechanism; every significant
  harness file should appear there with a precise trigger condition.

---

## Skills (`.agents/skills/<name>/`)

**When to create a project skill:**
- A multi-step workflow is repeated and benefits from consistent execution
- The agent makes consistent errors without explicit instruction
- A procedure has ≥ 3 non-obvious steps or critical ordering requirements
- Active governance mode: the 3× rule has been triggered

**Minimum structure:**

```
.agents/skills/<name>/
├── SKILL.md          ← required
├── references/       ← only if on-demand reference material is needed
└── assets/           ← only if structural templates are needed
```

**Project SKILL.md guidelines:**
- `name` must exactly match the parent directory name
- `description`: third person capability statement + imperative "Use when…" covering
  indirect trigger phrasings; 1–1024 chars
- Body: self-contained — no references to files outside `.agents/skills/<name>/`
- Body target: ≤ 200 lines (project skills are simpler than library skills)
- Gotchas section required: project-specific non-obvious facts only

**Naming:** lowercase a-z, digits 0-9, hyphens only; no leading/trailing/consecutive
hyphens; max 64 chars; must match directory name exactly.

---

## Knowledge Base

Default location: `.agents/knowledge/`. Always check for an existing `docs/`, `ADR/`,
or similar convention before choosing a location; consolidate rather than split.

The KB is a collection of distinct file types. Include only those the project needs;
these are common examples — other file types may be appropriate for your project.

### External References

**Files:** `REFERENCES.md` or `references/` folder

- `REFERENCES.md`: a curated list of external doc URLs; prefer links to `llms.txt`
  endpoints (e.g., `https://docs.example.com/llms.txt`) over HTML pages — agents
  parse plain text more reliably
- `references/` folder: for copied or downloaded reference files (copy `llms.txt`
  directly into the folder); use when offline access or version pinning is needed
- External docs can also be exposed via MCP instead of or in addition to files
- Add a row to the AGENTS.md when-to-read-what table pointing to the file or folder

**Single-file vs folder:** single `REFERENCES.md` for a short URL list; `references/`
folder when storing multiple copied documents.

### Plans

**Files:** `PLAN.md` or `plan/` folder

- Records current project plans, milestones, and open decisions
- If using an external PM tool (Linear, Jira, GitHub Projects) via MCP: keep a `PLAN.md`
  that describes how to access and interpret the MCP-managed plan, rather than
  duplicating plan content in files
- Agents should read this before starting work that may overlap with open tasks

**Single-file vs folder:** single `PLAN.md` unless the project has multiple parallel
work streams that benefit from separate files.

### Workflows / SOPs

**Files:** `WORKFLOW.md` or `workflow/` folder

- Describes operation procedures step-by-step; functions as a lightweight alternative
  to a full skill for projects not using self-evolution or Active governance
- Reference from AGENTS.md with a precise pointer:
  - Single file: file + section heading (e.g., 'search for `## Deploy Process` in `WORKFLOW.md`')
  - Folder: `workflow/deploy.md` (file path)
- When a workflow grows complex enough to benefit from skill structure (Gotchas,
  conditional references, assets), migrate it to `.agents/skills/<name>/`

**Single-file vs folder:** single `WORKFLOW.md` for one or two processes; `workflow/`
folder when each process deserves its own file.

### Specifications

**Files:** `SPEC.md` or `spec/` folder

- Stores product and technical requirements agents should respect
- Agents read this when implementing features or making scope decisions

**Single-file vs folder:** single `SPEC.md` for a contained scope; `spec/` folder
for multi-domain or multi-milestone specifications.

### Quality

**File:** `QUALITY.md` (always single file)

- Code quality standards: style rules, complexity limits, test coverage requirements
- Security requirements: input validation, auth patterns, forbidden patterns
- Agents must read this before writing or reviewing any production code

---

## Root-level Convention Files

These files live at the project root (not inside `.agents/`) and follow widely
recognized naming conventions.

### ARCHITECTURE.md

- Describes technical architecture: directory ownership, module boundaries, data
  flow, build and deploy topology
- Include: component diagram or tree, ownership map, non-obvious dependencies,
  cross-cutting concerns (logging, auth, error handling)
- Agents load this when making structural changes, adding new modules, or resolving
  cross-component questions
- Keep at project root alongside AGENTS.md

### DESIGN.md

- Defines frontend visual specifications: component library, token system, layout
  rules, interaction patterns
- Follows the [Stitch design-md format](https://stitch.withgoogle.com/docs/design-md/overview.md)
- Create only for projects with a visual/UI component; omit for backend-only or CLI
  projects
- Agents generating UI code or reviewing design implementations must read this first

**AGENTS.md integration for root-level files:** both ARCHITECTURE.md and DESIGN.md
(when present) must appear in the AGENTS.md when-to-read-what table with specific
trigger conditions.

---

## Quality Tools

**Minimum requirements for Thick harness:**
- Linter for the primary language — must run in CI pre-merge
- Formatter with committed project-level config (not editor-local)
- At least one harness-specific structural check

**Required harness checks:**
- AGENTS.md line count ≤ 150
- All relative paths referenced in SKILL.md files resolve to actual files
- No empty `.agents/` subdirectories

**Integration gates:**
- CI (pre-merge): linter + formatter + harness structural checks
- Pre-commit hook: formatter + AGENTS.md line count check

Both gates are required for Thick harness. Skipping either creates a drift window
between local state and CI-enforced state.

---

## Hooks

**Purpose:** runtime callbacks that correct specific, documented recurring error
patterns. Add a hook only when a recurring error has been observed and the correction
is deterministic.

**Hook placement by agent framework:**

| Framework | Hook file | Scope |
|---|---|---|
| GitHub Copilot | `.github/copilot-instructions.md` or workspace `.instructions.md` | Repo-wide or workspace |
| Cursor | `.cursor/rules/*.md` | Workspace |
| Claude Code | `CLAUDE.md` at repo root or per-directory | Directory tree |
| Windsurf | `.windsurfrules` | Workspace |
| Generic | Document in a KB file as a "pattern correction" entry | Reference only |

**Hook content rules:**
- One hook = one specific observed error + one deterministic correction
- Hooks must not duplicate AGENTS.md content — choose one location
- If the framework doesn't support hooks, document the pattern in a `runbook-` KB file
- Hooks with side effects (file writes, API calls) require explicit user authorization
