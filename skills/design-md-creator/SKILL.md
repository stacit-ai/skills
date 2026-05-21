---
name: design-md-creator
description: >
  Guides coding agents in designing, creating, and modifying a project's DESIGN.md file.
  Use when asked to "create a DESIGN.md", "scaffold a design system", "write visual styling rules",
  "lint my design tokens", or when asked to set up design guidelines, brand identity specifications,
  or export design tokens for a project.
---

# DESIGN.md Creator

This skill guides you through establishing, structuring, and maintaining a `DESIGN.md` file in a project root. A `DESIGN.md` serves as a single visual source of truth that humans and AI agents can seamlessly read, evolve, and apply to generate brand-compliant, high-quality, and accessible user interfaces.

## Step-by-step Workflow

Follow these steps when creating or modifying a design system in `DESIGN.md`:

### Step 1 — Discover Brand & Requirements
Before writing any token or prose, gather and inspect existing design contexts in this order:
1.  **Codebase Styling**: Check for CSS files (e.g., `index.css`, `styles.css`), Tailwind configurations (`tailwind.config.js`), or component folders to identify current color palettes, font families, and shape roundness.
2.  **User Preferences**: Read user instructions, design mockups, or UI style guides provided in the prompt or repository documentation.
3.  **Default Palette**: If no brand guidelines exist, choose a cohesive, harmonious palette (e.g., primary, secondary, neutral) matching the app's domain (e.g., deep blue and warm neutral for enterprise, vibrant emerald for creative/eco-friendly).

### Step 2 — Draft the Design Tokens (YAML)
Establish the machine-readable design system tokens in the YAML front matter:
1.  **Boilerplate Setup**: Load `assets/boilerplate.md` if starting a new design system file.
2.  **Define Colors**: Establish the hex colors in the `colors` group. Ensure a `primary` color is defined.
3.  **Define Typography**: Map key text elements (e.g., `h1`, `body-md`, `label-caps`) in the `typography` group with properties like `fontFamily` and `fontSize`.
4.  **Define Spacing and Rounded Scales**: Define standard scales for paddings/margins (`spacing`) and corner roundness (`rounded`).
5.  **Map Component Styles**: Define token values or references (using `{colors.primary}`, etc.) for specific UI atoms in the `components` group.
6.  *Actionable Guidance*: For detailed syntax and constraints, load [references/token-schema.md](references/token-schema.md).

### Step 3 — Compose Prose & Visual Rationale (Markdown)
Develop the human-readable Markdown body that provides context and guidance on how to apply the tokens:
1.  **Canonical Order**: Write the visual rationale sections using `##` headings in exact sequence: `Overview`, `Colors`, `Typography`, `Layout`, `Elevation & Depth`, `Shapes`, `Components`, `Do's and Don'ts`.
2.  **Write Prose Description**: In each section, explain the "why" and "how" behind the tokens, providing rules for when and where each token should be utilized.
3.  *Actionable Guidance*: For details on section writing rules, aliases, and examples, load [references/sections.md](references/sections.md).

### Step 4 — Validate Using the CLI
Verify the completed `DESIGN.md` structure, syntax, and accessibility:
1.  **Run Lint Command**: Run `npx -y @google/design.md lint DESIGN.md` to analyze structure, contrast ratios, and token references.
2.  **Address Errors & Warnings**:
    *   Fix any `broken-ref` errors immediately (e.g. broken token paths).
    *   Resolve `contrast-ratio` warnings if background/text colors fall below the 4.5:1 ratio.
    *   Check for `orphaned-tokens` (tokens defined but never referenced) and clean up.
3.  *Actionable Guidance*: For complete CLI usage details, options, and rules description, load [references/cli.md](references/cli.md).

---

## Gotchas

- **Strict Hex Format**: All color values in the YAML front matter must strictly be in sRGB `#` + hex format (e.g. `"#1A1C1E"`). Short hexes (e.g. `"#fff"`) or functions (e.g. `rgb()`, `hsl()`) are invalid and fail linting.
- **Reference Wrapping**: Token references MUST be wrapped in curly braces (e.g., `"{colors.primary}"`). Forgetting braces (e.g., `colors.primary`) is treated as a literal string.
- **Canon Sequence**: Sections are strictly ordered. Even if some sections are omitted, those present must follow the canonical sequence. Placing a `## Layout` section before `## Colors` will trigger a lint warning.
- **Component Token Boundaries**: Property names under component keys are restricted to the standard set: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Standardize on these keys; other keys will trigger warnings.
- **Numeric Font Weights**: The `fontWeight` property in typography must use a numeric weight (e.g., `400`, `600`, `700`). Do not use named string values like `"bold"` or `"regular"`; quoted numeric values are acceptable if allowed by the token schema.
- **WCAG Contrast Ratios**: A primary button or text container defining `backgroundColor` and `textColor` must meet the WCAG AA minimum contrast ratio of 4.5:1. Ensure accessible combinations are chosen.
- **Non-Interactive npx execution**: When validating or exporting using the CLI in agent environments, always append the `-y` flag (e.g., `npx -y @google/design.md`) to bypass any package installation prompts.

---

## References

- Load [references/token-schema.md](references/token-schema.md) when defining, editing, or auditing YAML front matter design tokens.
- Load [references/sections.md](references/sections.md) when writing or structuring the human-readable Markdown body sections.
- Load [references/cli.md](references/cli.md) when invoking, validating, or explaining the `@google/design.md` CLI commands and linting rules.
- Load [assets/boilerplate.md](assets/boilerplate.md) when scaffolding a brand-new `DESIGN.md` file.
