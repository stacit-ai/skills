# [Project Name]

## Purpose

[One sentence: what this project does and its primary domain.]

## Structure

```
[root]/
├── [dir1]/         ← [one-line description]
├── [dir2]/         ← [one-line description]
│   └── [subdir]/   ← [one-line description]
└── [file]          ← [one-line description]
```

## Core Conventions

- **Language**: [primary language and version]
- **Style**: [formatter/linter name and key rules]
- **Naming**: [key naming convention, e.g., kebab-case files, PascalCase classes]
- **Commits**: [commit format, e.g., Conventional Commits]

## When to Read What

KB files, workflow files, spec files, plan files, and root-level convention files
(ARCHITECTURE.md, DESIGN.md) are not auto-discovered — include them here so agents
entering via AGENTS.md know to look for them. For multi-file domains a folder pointer
is sufficient; listing every individual file is not required.

Skills, hooks, and MCP configs are **auto-discovered** by the agent framework via
their `description` fields or placement locations — omit them from this table (the
framework loads them without harness registration). You may include a skill row as
human-readable context, but it is not required for framework loading.

| Read | When |
|---|---|
| `ARCHITECTURE.md` | when making structural or cross-cutting changes |
| `DESIGN.md` | when generating or reviewing UI code *(omit if no UI)* |
| `.agents/knowledge/[file]` | [specific question or task] |
| `WORKFLOW.md` or `workflow/[file]` | [specific operation this SOP covers] |
| `SPEC.md` or `spec/` | when implementing features or clarifying scope |
| `QUALITY.md` | when writing or reviewing production code |
| `REFERENCES.md` or `references/` | when needing external API or library docs |
| `PLAN.md` or `plan/` | before starting any new task |

*(Remove rows for files that don't exist in this project.)*

## Keep in Sync

*(For Light projects: embed the sync table below. When the table would overflow the
AGENTS.md budget, move detailed sync rules to a workflow or reference file and leave
per-concern pointer lines here instead — each with its own trigger condition, for
example: `- When adding a new API endpoint, see WORKFLOW.md §API Conventions`. For
Medium projects: replace the detailed table with per-concern pointer rows in the
when-to-read-what table, each with its own trigger condition and pointing to the
dedicated sync reference file or section for that concern; do not use a single
generic pointer row for all sync concerns. For Thick/Active projects: remove this
section; consistency is maintained by per-concern sync skills created with the
`harness-sync` skill — loaded automatically by the agent framework. When a new
consistency concern arises, use `harness-sync` to create a dedicated sync skill.)*

| When this changes | Update this |
|---|---|
| Directory structure | AGENTS.md §Structure section |
| File or API renamed | All `.agents/` files that reference the old name |
| Convention changed | AGENTS.md §Core Conventions + relevant KB file |
| Security rule changed | `QUALITY.md` or relevant knowledge base file |

## Validation

| Command | Scope |
|---|---|
| `[command]` | [what it checks] |
