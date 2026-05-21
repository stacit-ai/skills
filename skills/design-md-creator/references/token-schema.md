# DESIGN.md Token Schema Reference

Design tokens are embedded as YAML front matter at the very beginning of the `DESIGN.md` file. The front matter block must start with a line containing exactly `---` and end with a line containing exactly `---`.

## YAML Schema Outline

```yaml
version: alpha             # optional, current version: "alpha"
name: <string>             # required, name of the design system
description: <string>      # optional, high-level description
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

---

## Token Types and Constraints

### 1. Color
Must strictly be a string starting with `#` followed by a hex color code in the sRGB color space.
-   **Valid**: `"#1A1C1E"`, `"#B8422E"`, `"#FFFFFF"`
-   **Invalid**: `"#fff"` (shorthand not supported), `"red"`, `"rgb(26, 28, 30)"`, `"hsl(210, 8%, 10%)"`

### 2. Dimension
A dimension value is a string with a numeric value followed immediately by a unit suffix. Valid unit suffixes are: `px`, `em`, `rem`.
-   **Valid**: `4px`, `1.5rem`, `0.75em`, `-0.02em`
-   **Invalid**: `4` (unitless dimension), `4 px` (spaces not allowed), `4vh`, `4vw`

### 3. Typography Object
A complex token representing font properties. It accepts the following keys:
-   `fontFamily` (string): The font name (e.g. `Public Sans`, `Roboto`).
-   `fontSize` (Dimension): E.g., `48px`, `1rem`.
-   `fontWeight` (number): A numeric font weight value (e.g. `400`, `600`, `700`). In YAML, this can be expressed as a raw number or quoted string.
-   `lineHeight` (Dimension | number): A Dimension (e.g., `24px`, `1.5rem`) or a unitless multiplier (e.g. `1.6`).
-   `letterSpacing` (Dimension): E.g., `-0.02em`, `0.1em`.
-   `fontFeature` (string): Configures `font-feature-settings` (e.g., `"'liga' on, 'calt' on"`).
-   `fontVariation` (string): Configures `font-variation-settings`.

### 4. Spacing Scale
A map from a scale level key (e.g. `xs`, `sm`, `md`, `lg`, `xl`, `gutter`, `margin`) to a `Dimension` or unitless `number` (e.g., column span or ratio).
-   **Example**:
    ```yaml
    spacing:
      xs: 4px
      sm: 8px
      md: 16px
      lg: 32px
      columns: 12
    ```

### 5. Rounded Scale
A map from a corner radius level key (e.g. `sm`, `md`, `lg`, `full`) to a `Dimension`.
-   **Example**:
    ```yaml
    rounded:
      sm: 4px
      md: 8px
      lg: 12px
      full: 9999px
    ```

---

## Token Reference Syntax

You can cross-reference other tokens within the YAML tree by wrapping the absolute dot-notation path in curly braces:
-   `"{colors.primary}"`
-   `"{typography.h1}"`
-   `"{rounded.md}"`

### Reference Rules:
1.  **Strict Quotes**: In YAML, always wrap references in quotation marks to prevent parser issues with curly braces (e.g. `backgroundColor: "{colors.primary}"`).
2.  **Primitive vs Composite**:
    *   For most token groups (e.g. `rounded`, `spacing`), references must point to primitive leaf values (like a color hex string or a single dimension).
    *   Within the `components` section, references to composite values (e.g. `{typography.body-md}`) are permitted to map typography blocks cleanly.

---

## Component Mapping & Properties

The `components` section defines style overrides and mappings for specific UI atoms and their states (e.g. hover, active).

### Allowed Component Keys
Property keys inside a component block are strictly limited to the following set:
-   `backgroundColor`: `<Color>` or reference to Color.
-   `textColor`: `<Color>` or reference to Color.
-   `typography`: `<Typography>` or reference to Typography.
-   `rounded`: `<Dimension>` or reference to Rounded.
-   `padding`: `<Dimension>` or reference to Spacing/Dimension.
-   `size`: `<Dimension>` or reference to Dimension.
-   `height`: `<Dimension>` or reference to Dimension.
-   `width`: `<Dimension>` or reference to Dimension.

### Variants naming:
Component states and variants are represented as separate component keys using a logical suffix:
```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-dark}"
  button-primary-disabled:
    backgroundColor: "{colors.neutral-gray}"
    textColor: "{colors.neutral-dark}"
```
