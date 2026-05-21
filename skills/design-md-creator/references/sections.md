# DESIGN.md Sections & Formatting Reference

Every `DESIGN.md` file must follow a strict heading structure. Sections use `##` (H2) headings. You can omit sections if they do not apply to the project, but the sections present must follow the sequence below.

---

## Canonical Section Order

| Heading Name | Allowed Aliases | Description |
|:---|:---|:---|
| `## Overview` | `## Brand & Style` | Brand personality, target audience, and emotional/visual vibes. |
| `## Colors` | None | Narrative color palette description, roles, and semantic meanings. |
| `## Typography` | None | Rationale for typefaces, pairings, label guidelines, and hierarchies. |
| `## Layout` | `## Layout & Spacing` | Layout model (grids, safe areas), padding strategies, and rhythm. |
| `## Elevation & Depth` | `## Elevation` | Visual hierarchy mechanics (shadows, elevations) or flat layer rules. |
| `## Shapes` | None | Visual geometry rules (rounding, sharpness, borders). |
| `## Components` | None | Styling rules and properties for common atoms (buttons, fields, lists). |
| `## Do's and Don'ts` | None | Clear visual dos and don'ts as bulleted lists. |

---

## Section Guidelines & Details

### 1. Overview
Defines the brand's visual identity.
-   Describe the brand's "vibe" (e.g. "matte newsroom", "glassmorphism dashboard", "playful candy-colored web app").
-   Define the target audience and desired emotional response (e.g., trust, excitement, precision, calmness).

### 2. Colors
Explains the visual roles of the color tokens.
-   Identify semantic color roles (primary, secondary, accent, surface, error).
-   Provide names and descriptions for primary colors (e.g. `"*Neutral (#F7F5F2):* Warm limestone foundation"`).

### 3. Typography
Describes the typography pairing rules.
-   Detail the typefaces used and their emotional intent (e.g. "Public Sans for readability and Space Grotesk for stopwatch precision").
-   Clarify the hierarchies and styles (e.g. "h1 is set in semibold to establish trustworthiness").

### 4. Layout & Spacing
Defines how space is divided and elements are grouped.
-   Detail the layout grid (e.g. "12-column grid for desktop, fluid vertical flow for mobile").
-   Define spacing rhythm principles (e.g., "8px spacing grid with 4px micro-steps").

### 5. Elevation & Depth
Explains how depth and layering are achieved.
-   For elevated systems: describe shadows, drop-shadow styling (blur, color, spread).
-   For flat/semi-flat systems: explain alternative layer distinctions (e.g. "tonal layers where background is off-white and content is pure white").

### 6. Shapes
Describes the aesthetic form and border styles.
-   Outline corner radius rules (e.g., "minimal 4px rounding to feel sharp yet modern").
-   State border guidelines (e.g. "1px borders in secondary neutral for light containers").

### 7. Components
Detailed styling requirements for UI components.
-   Provide explicit guidance for atoms:
    *   **Buttons**: padding, roundness, text case, states (hover, pressed, focus).
    *   **Inputs**: background, border states, focus rings, helper text.
    *   **Tooltips & Badges**: styling and visual grouping rules.

### 8. Do's and Don'ts
Actionable rules to prevent design regressions.
-   Use clear, positive bullet points for **Do's** and negative bullet points for **Don'ts**.
-   **Example**:
    ```markdown
    ## Do's and Don'ts

    - Do maintain a 4.5:1 contrast ratio for all readable text.
    - Don't mix sharp and fully rounded inputs in the same view.
    - Do limit font weights to a maximum of three styles on one screen.
    - Don't use primary brand colors on non-interactive elements.
    ```
