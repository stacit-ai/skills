# DESIGN.md CLI & Rules Reference

The official CLI tool `@google/design.md` helps you validate, diff, and export design systems defined in `DESIGN.md`.

## Execution in Agent Environments

Always run the CLI tool using `npx -y @google/design.md` to automatically download the package and execute it in non-interactive mode.

---

## Commands & Usage

### 1. `lint`
Validates a `DESIGN.md` file for structural and grammatical correctness and checks contrast rules.
```bash
npx -y @google/design.md lint [OPTIONS] <FILE>
```
-   **Arguments**:
    *   `FILE`: Path to the target `DESIGN.md` file (use `-` for stdin).
-   **Options**:
    *   `--format="json" | "text"`: Format the diagnostic findings (default is `json`).

**Example JSON Output**:
```json
{
  "findings": [
    {
      "severity": "warning",
      "path": "components.button-primary",
      "message": "textColor (#ffffff) on backgroundColor (#1A1C1E) has contrast ratio 15.42:1 — passes WCAG AA."
    }
  ],
  "summary": { "errors": 0, "warnings": 1, "info": 1 }
}
```

### 2. `diff`
Compares two versions of a design system to trace changes and detect visual regressions.
```bash
npx -y @google/design.md diff [OPTIONS] <BEFORE> <AFTER>
```
-   **Arguments**:
    *   `BEFORE`: Path to the baseline/original `DESIGN.md` file.
    *   `AFTER`: Path to the updated/new `DESIGN.md` file.
-   **Options**:
    *   `--format="json" | "text"`: Format the results output (default is `json`).

### 3. `export`
Converts design system tokens into configurations for popular tools.
```bash
npx -y @google/design.md export [OPTIONS] <FILE> --format <tailwind | dtcg>
```
-   **Arguments**:
    *   `FILE`: Path to `DESIGN.md` (use `-` for stdin).
-   **Options**:
    *   `--format <tailwind | dtcg>` (required): Choose target output format (Tailwind CSS configuration or W3C DTCG JSON).

### 4. `spec`
Prints the DESIGN.md format specification and linting rules.
```bash
npx -y @google/design.md spec [OPTIONS]
```
-   **Options**:
    *   `--rules`: Append the active linting rules table.
    *   `--rules-only`: Print ONLY the linting rules table.

---

## Active Linting Rules

When you run `lint`, the CLI evaluates your file against the following rules:

| Rule Name | Severity | Description |
|:---|:---|:---|
| `broken-ref` | **Error** | Checks for broken/circular token references and unknown sub-tokens in the `components` mapping. |
| `missing-primary` | **Warning** | Triggers if the `colors` group is defined but has no token named `primary`. |
| `contrast-ratio` | **Warning** | Analyzes the `textColor` and `backgroundColor` pairs in component style mappings. Emits a warning if the contrast falls below the WCAG AA minimum of **4.5:1** for readable text. |
| `orphaned-tokens` | **Warning** | Identifies tokens defined in front matter that are never referenced by components. |
| `missing-typography` | **Warning** | Triggers if a `colors` palette is defined but no typography tokens are set up. |
| `section-order` | **Warning** | Checks if H2 sections inside the Markdown body are arranged in the canonical sequence. |
| `token-summary` | **Info** | Outputs a diagnostic summary of the counts of defined tokens. |
| `missing-sections` | **Info** | Reports when standard optional sections (like `spacing` or `rounded`) are absent from tokens. |
