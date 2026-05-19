#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "detect-secrets>=1.4,<2",
# ]
# requires-python = ">=3.11"
# ///
"""Scan files or inline text for secrets and credentials using detect-secrets.

Inline text is written to a temporary file, scanned, then the temp file is
immediately deleted regardless of scan outcome.

Exit codes:
  0  scan completed (findings list may be empty)
  1  dependency or scan error
  2  invalid arguments
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path


def _run_detect_secrets(scan_paths: list[str]) -> dict:
    """Invoke detect-secrets via subprocess and return the parsed JSON output.

    Tries `detect-secrets scan` first, then falls back to
    `python -m detect_secrets scan` if the entry-point binary is not on PATH.
    Returns a dict with an "error" key if both attempts fail.
    """
    import subprocess

    for cmd_prefix in (
        ["detect-secrets", "scan"],
        [sys.executable, "-m", "detect_secrets", "scan"],
    ):
        try:
            result = subprocess.run(
                cmd_prefix + scan_paths,
                capture_output=True,
                text=True,
                check=False,
            )
            # detect-secrets exits 0 on success; treat 1 as "ran but found issues"
            if result.returncode not in (0, 1):
                continue
            if not result.stdout.strip():
                continue
            return json.loads(result.stdout)
        except FileNotFoundError:
            continue
        except json.JSONDecodeError as exc:
            return {"error": f"failed to parse detect-secrets output: {exc}"}

    return {
        "error": (
            "detect-secrets command not found. "
            "Ensure it is installed: uv run --with detect-secrets ... "
            "or pip install detect-secrets"
        )
    }


def _normalize(raw: dict, label_map: dict[str, str] | None = None) -> list[dict]:
    """Flatten detect-secrets results into a uniform list of finding dicts."""
    findings = []
    for filepath, secrets in raw.get("results", {}).items():
        display = (label_map or {}).get(filepath, filepath)
        for secret in secrets:
            findings.append(
                {
                    "file": display,
                    "line": secret.get("line_number"),
                    "type": secret.get("type", "Unknown"),
                    "is_verified": secret.get("is_verified", False),
                    "hashed_secret": secret.get("hashed_secret", ""),
                }
            )
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Scan files or inline text for secrets and credentials "
            "using detect-secrets."
        ),
        epilog=(
            "Examples:\n"
            "  uv run scripts/secret_scan.py --file config.py .env\n"
            "  uv run scripts/secret_scan.py --text 'api_key = \"sk-abc123xyz\"'"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--file",
        nargs="+",
        metavar="FILE",
        help="One or more file paths to scan.",
    )
    parser.add_argument(
        "--text",
        metavar="TEXT",
        help="Inline text to scan (written to a temp file, deleted after scan).",
    )
    args = parser.parse_args()

    if not args.file and args.text is None:
        parser.error("Provide --file, --text, or both.")

    label_map: dict[str, str] = {}
    scan_paths: list[str] = []
    tmp_path: str | None = None

    # Write inline text to a temp file so detect-secrets can process it
    if args.text is not None:
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".txt",
                prefix="sig_scan_",
                delete=False,
                encoding="utf-8",
            ) as tmp:
                tmp.write(args.text)
                tmp_path = tmp.name
            label_map[tmp_path] = "<inline-text>"
            scan_paths.append(tmp_path)
        except OSError as exc:
            print(f"Failed to create temp file: {exc}", file=sys.stderr)
            sys.exit(1)

    if args.file:
        missing = [f for f in args.file if not Path(f).exists()]
        if missing:
            if tmp_path:
                Path(tmp_path).unlink(missing_ok=True)
            parser.error(f"File(s) not found: {', '.join(missing)}")
        scan_paths.extend(args.file)

    raw = _run_detect_secrets(scan_paths)

    # Always clean up temp file before reporting errors
    if tmp_path:
        Path(tmp_path).unlink(missing_ok=True)

    if "error" in raw:
        print(raw["error"], file=sys.stderr)
        sys.exit(1)

    findings = _normalize(raw, label_map)

    sources: list[str] = []
    if args.text is not None:
        sources.append("<inline-text>")
    if args.file:
        sources.extend(args.file)

    print(
        json.dumps(
            {
                "sources": sources,
                "finding_count": len(findings),
                "findings": findings,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
