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

Every harness layer or domain must be discoverable through this table. For
multi-file domains, a hierarchical folder pointer is sufficient — list the folder,
not every file within it. Any layer not represented here is invisible to agents
entering via AGENTS.md.

| Read | When |
|---|---|
| `ARCHITECTURE.md` | when making structural or cross-cutting changes |
| `DESIGN.md` | when generating or reviewing UI code *(omit if no UI)* |
| `.agents/skills/[name]/` | [specific task this skill covers] |
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
