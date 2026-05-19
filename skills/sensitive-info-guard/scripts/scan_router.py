#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "tiktoken>=0.7,<1",
# ]
# requires-python = ">=3.11"
# ///
"""Classify text or files for sensitive-info-guard scan routing.

Each item is classified as:
  deep   — token count <= threshold: suitable for direct LLM deep read
  script — token count >  threshold: use scan scripts for quick analysis
  binary — non-UTF-8 file: cannot be scanned as text

Falls back to character-count estimation (1 token ≈ 4 chars) if tiktoken
is unavailable or fails to load.

Exit codes:
  0  classification successful (all items resolved)
  1  one or more input paths were not found
  2  invalid arguments
"""

import argparse
import json
import sys
from pathlib import Path

BINARY_PROBE_BYTES = 8192
CHARS_PER_TOKEN_FALLBACK = 4  # rough approximation used when tiktoken is unavailable


def _load_encoding():
    """Return a tiktoken Encoding, or None if unavailable."""
    try:
        import tiktoken
        return tiktoken.get_encoding("cl100k_base")
    except Exception as exc:
        print(
            f"tiktoken unavailable ({exc}); falling back to character-count estimate.",
            file=sys.stderr,
        )
        return None


def _count_tokens(text: str, encoding) -> tuple[int, bool]:
    """Return (token_count, is_estimated).

    is_estimated is True when tiktoken is not available and the count is
    approximated from character length.
    """
    if encoding is not None:
        try:
            return len(encoding.encode(text)), False
        except Exception as exc:
            print(f"tiktoken encode failed ({exc}); using estimate.", file=sys.stderr)
    return max(1, len(text) // CHARS_PER_TOKEN_FALLBACK), True


def _is_binary(path: Path) -> bool:
    """Return True if the file cannot be decoded as UTF-8 text."""
    try:
        with path.open("rb") as file_obj:
            file_obj.read(BINARY_PROBE_BYTES).decode("utf-8")
        return False
    except UnicodeDecodeError:
        return True


def _classify_text(text: str, threshold: int, encoding) -> dict:
    token_count, estimated = _count_tokens(text, encoding)
    result: dict = {
        "item": "<inline-text>",
        "token_count": token_count,
        "estimated": estimated,
        "method": "script" if token_count > threshold else "deep",
    }
    if estimated:
        result["note"] = (
            f"token count estimated from character length "
            f"({len(text)} chars ÷ {CHARS_PER_TOKEN_FALLBACK}); tiktoken unavailable"
        )
    return result


def _classify_file(path: Path, threshold: int, encoding) -> dict:
    if not path.exists():
        return {"item": str(path), "error": "file not found"}

    if _is_binary(path):
        return {
            "item": str(path),
            "token_count": None,
            "estimated": False,
            "method": "binary",
            "note": "binary or non-UTF-8 file; text content cannot be extracted",
        }

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"item": str(path), "error": f"could not read file: {exc}"}

    token_count, estimated = _count_tokens(text, encoding)
    result: dict = {
        "item": str(path),
        "token_count": token_count,
        "estimated": estimated,
        "method": "script" if token_count > threshold else "deep",
    }
    if estimated:
        result["note"] = (
            f"token count estimated from character length "
            f"({len(text)} chars ÷ {CHARS_PER_TOKEN_FALLBACK}); tiktoken unavailable"
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Classify text or files as 'deep', 'script', or 'binary' "
            "based on GPT-4 token count. Used by sensitive-info-guard "
            "to decide whether to scan with an LLM or with scripts."
        ),
        epilog=(
            "Examples:\n"
            "  uv run scripts/scan_router.py --files README.md src/config.py\n"
            "  uv run scripts/scan_router.py --text 'User email: bob@example.com'\n"
            "  uv run scripts/scan_router.py --files data.csv --threshold 2000"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--files",
        nargs="+",
        metavar="FILE",
        help="One or more file paths to classify.",
    )
    parser.add_argument(
        "--text",
        metavar="TEXT",
        help="Inline text string to classify.",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=4000,
        metavar="N",
        help=(
            "Token count threshold (default: 4000, GPT-4 cl100k_base tokens). "
            "Items above this are routed to 'script'; at or below to 'deep'."
        ),
    )
    args = parser.parse_args()

    if not args.files and args.text is None:
        parser.error("Provide --files, --text, or both.")

    encoding = _load_encoding()
    results: list[dict] = []
    has_error = False

    if args.text is not None:
        results.append(_classify_text(args.text, args.threshold, encoding))

    if args.files:
        for fstr in args.files:
            r = _classify_file(Path(fstr), args.threshold, encoding)
            if "error" in r:
                has_error = True
                print(f"Error: {r['error']} ({fstr!r})", file=sys.stderr)
            results.append(r)

    print(json.dumps(results, indent=2))
    sys.exit(1 if has_error else 0)


if __name__ == "__main__":
    main()
