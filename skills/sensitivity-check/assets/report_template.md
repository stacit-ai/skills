# Sensitive Information Scan Report

## Scan Summary

- **Scan Date:** {YYYY-MM-DD}
- **Check Types:** {PII / Secrets / Both}
- **Items Scanned:** {N} item(s)
- **Check Method Used:** {Deep read / Script scan / Mixed}
- **Binary Files Skipped:** {N or "None"}

## Items Scanned

| # | Item | Type | Token Count | Method |
|---|---|---|---|---|
| 1 | {file path or "inline text"} | {file / text} | {N or "N/A (binary)"} | {deep / script / binary} |

## Findings

{If no findings across all items, write: "No findings."}

| # | Source | Severity | Type | Location | Excerpt | Status |
|---|---|---|---|---|---|---|
| 1 | {file path or "inline text"} | {Critical / High / Medium / Low} | {entity type} | {Line N / Char N–N} | `{excerpt with sensitive value in [brackets]}` | {Confirmed / False Positive} |

**Finding #1 — False Positive Reason** *(include only when Status = False Positive)*:
{Reason, e.g., "Example email address in documentation; labeled as illustrative."}

## False Positives Summary

{List all false positives across all items. If none, write: "No false positives identified."}

| Item | Type | Location | Reason |
|---|---|---|---|
| {file/text} | {type} | {location} | {reason} |

## Binary Files (Not Analyzed)

{List file paths of binary files that could not be scanned as text. If none, write: "None."}

- `{file path}` — binary file; text content not extractable

## Conclusion

**Contains sensitive information: {YES / NO}**

{If YES:}
Confirmed {N} finding(s) after false-positive review: {brief summary — what types were
found, in which files/locations, and the highest severity level present.}

{If NO:}
No confirmed sensitive information was found. {If false positives were present, add:}
{N} potential match(es) were reviewed and determined to be false positives
({brief reason, e.g., "example values in documentation, test fixture data"}).
