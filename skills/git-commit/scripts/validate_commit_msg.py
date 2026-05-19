#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# ///
"""Validate a git commit message against the 50/72 rule and basic style conventions.

Rules enforced:
  1. Title line must not be empty
  2. Title line must be <= 50 characters
  3. Title must not end with a period
  4. When a body is present, line 2 must be blank (title/body separator)
  5. All body lines must be <= 72 characters

Exit codes:
  0  message is valid
  1  one or more validation errors found
  2  invalid arguments

Output (stdout): JSON object
  {"valid": bool, "errors": [{"line": int, "rule": str, "message": str}]}
"""

import argparse
import json
import sys
from pathlib import Path


def validate(message: str) -> list[dict]:
    errors: list[dict] = []
    lines = message.splitlines()

    if not lines or not message.strip():
        errors.append(
            {
                "line": 1,
                "rule": "title-not-empty",
                "message": "Commit message must not be empty",
            }
        )
        return errors

    title = lines[0].rstrip()

    if not title.strip():
        errors.append(
            {
                "line": 1,
                "rule": "title-not-empty",
                "message": "Title line must not be empty",
            }
        )
        return errors

    if len(title) > 50:
        errors.append(
            {
                "line": 1,
                "rule": "title-max-length",
                "message": (
                    f"Title is {len(title)} characters; must be <= 50. "
                    f'Current title: "{title}"'
                ),
            }
        )

    if title.endswith("."):
        errors.append(
            {
                "line": 1,
                "rule": "title-no-period",
                "message": "Title must not end with a period",
            }
        )

    # Check separator line when a body is present
    if len(lines) >= 2 and lines[1].strip():
        errors.append(
            {
                "line": 2,
                "rule": "blank-line-after-title",
                "message": (
                    "Line 2 must be blank to separate the title from the body; "
                    f'got: "{lines[1]}"'
                ),
            }
        )

    # Check body line lengths (lines 3 onwards, 1-indexed)
    for i, line in enumerate(lines[2:], start=3):
        if len(line) > 72:
            errors.append(
                {
                    "line": i,
                    "rule": "body-max-line-length",
                    "message": (
                        f"Line {i} is {len(line)} characters; body lines must be <= 72. "
                        f'Wrap at 72: "{line[:72]}..."'
                    ),
                }
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a git commit message against the 50/72 rule.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit codes:
  0  message is valid
  1  one or more validation errors found
  2  invalid arguments

Output (stdout): JSON
  {"valid": bool, "errors": [{"line": int, "rule": str, "message": str}]}

Rules checked:
  title-not-empty          Title must not be empty
  title-max-length         Title <= 50 characters
  title-no-period          Title does not end with a period
  blank-line-after-title   Line 2 must be blank when a body is present
  body-max-line-length     Body lines <= 72 characters

Examples:
  uv run validate_commit_msg.py --message "fix login redirect loop"
  uv run validate_commit_msg.py --file .git/COMMIT_EDITMSG
""",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--message",
        "-m",
        metavar="TEXT",
        help="Commit message text (use actual newlines or \\\\n for newlines)",
    )
    group.add_argument(
        "--file",
        "-f",
        metavar="PATH",
        help="Path to a file containing the commit message",
    )
    args = parser.parse_args()

    if args.file:
        try:
            message = Path(args.file).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(
                json.dumps({"error": f"File not found: {args.file}"}),
                file=sys.stderr,
            )
            sys.exit(2)
        except OSError as exc:
            print(json.dumps({"error": str(exc)}), file=sys.stderr)
            sys.exit(2)
    else:
        message = args.message.replace("\\n", "\n")

    errors = validate(message)
    result = {"valid": len(errors) == 0, "errors": errors}
    print(json.dumps(result, indent=2))

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
