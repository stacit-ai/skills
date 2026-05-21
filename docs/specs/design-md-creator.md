# Spec: design-md-creator

## Purpose

Guides an agent through creating or modifying a `DESIGN.md` file that conforms to the formal `DESIGN.md` format specification. The skill ensures that visual identities are structured in a standardized way so that downstream coding agents can generate high-quality, visually consistent, and on-brand UI components. It also helps validate design tokens against active accessibility rules (such as WCAG AA contrast ratios).

## Trigger Conditions

**Explicit:**
- "create a DESIGN.md"
- "scaffold a design system"
- "write a DESIGN.md file"
- "generate design tokens"
- "lint our DESIGN.md"
- "validate my design system tokens"

**Indirect (must also trigger):**
- "our app needs a cohesive design system"
- "add visual guidelines so agents know our styles"
- "make sure the AI knows what fonts and colors to use"
- "standardize visual styling rules"
- "export our design tokens to tailwind"

## What the Agent Lacks

Without this skill, an agent would likely:
- Use non-standard or out-of-order section headings, violating the canonical sequence.
- Omit the YAML front matter entirely or use an unstructured markdown format for tokens.
- Use invalid color formats (e.g. shorthand, names, or CSS functions like `rgb()`, `hsl()`) instead of the required sRGB `#RRGGBB` hex string.
- Forget the curly braces around token references (e.g. using `colors.primary` instead of `{colors.primary}`).
- Invent invalid or un-supported sub-token properties in the `components` section (e.g. `border-color` instead of standard camelCase properties).
- Design components without verifying if background/text pairs satisfy the WCAG AA minimum contrast ratio of 4.5:1.
- Not know how to use the `@google/design.md` CLI validator tool to automate structural and contrast linting.

## Scope

One coherent work unit: creating, formatting, or updating a single `DESIGN.md` file in a project repository.

Out of scope:
- Choosing or defining the project's brand identity itself. The brand and visual direction must be supplied by the user, design documents, or project context.
- Directly setting up build steps or Tailwind configurations (though generating the DESIGN.md is in scope, and generating tailwind config from it is a CLI function).

## External Dependencies

- `@google/design.md` CLI tool (invoked via `npx @google/design.md`).
- W3C Design Tokens Community Group (DTCG) specification.
