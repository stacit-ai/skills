#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "presidio-analyzer>=2.2,<3",
#   "spacy>=3.7,<4",
# ]
# requires-python = ">=3.11"
# ///
"""Scan text or a file for PII entities using presidio-analyzer.

On systems without CUDA, invoke via:
  uv run --extra-index-url https://download.pytorch.org/whl/cpu --with torch \\
    scripts/pii_scan.py ...

On systems with CUDA (nvidia-smi exits 0), invoke directly:
  uv run scripts/pii_scan.py ...

If presidio-analyzer or spacy is unavailable (uv run fails entirely), the script
exits with code 1 and prints fallback instructions to stderr. In that case, use
grep/regex patterns for a basic PII sweep instead.

Exit codes:
  0  scan completed (findings list may be empty)
  1  dependency or analysis error
  2  invalid arguments
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

CONTEXT_CHARS = 40  # surrounding characters included in each excerpt


def _ensure_spacy_model(model_name: str = "en_core_web_sm") -> bool:
    """Download the spacy model if not already present. Returns True on success."""
    try:
        import spacy
        spacy.load(model_name)
        return True
    except OSError:
        print(f"Downloading spacy model '{model_name}'...", file=sys.stderr)
        result = subprocess.run(
            [sys.executable, "-m", "spacy", "download", model_name],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return True
        print(
            f"Could not download spacy model '{model_name}': {result.stderr.strip()}",
            file=sys.stderr,
        )
        return False
    except ImportError:
        return False


def _excerpt(text: str, start: int, end: int, context: int = CONTEXT_CHARS) -> str:
    """Return a short excerpt with the matched span highlighted in [brackets]."""
    lo = max(0, start - context)
    hi = min(len(text), end + context)
    prefix = ("..." if lo > 0 else "") + text[lo:start]
    match = text[start:end]
    suffix = text[end:hi] + ("..." if hi < len(text) else "")
    return f"{prefix}[{match}]{suffix}"


def _scan(text: str, language: str, score_threshold: float) -> list[dict]:
    try:
        from presidio_analyzer import AnalyzerEngine
        from presidio_analyzer.nlp_engine import NlpEngineProvider
    except ImportError as exc:
        print(
            f"presidio-analyzer not available: {exc}\n"
            "On non-CUDA systems, run with:\n"
            "  uv run --extra-index-url https://download.pytorch.org/whl/cpu "
            "--with torch scripts/pii_scan.py ...\n"
            "If uv is unavailable, fall back to regex patterns for email, "
            "phone, IPv4/v6, and credit card numbers.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Use en_core_web_sm for lighter footprint (no transformer / CUDA dependency).
    # If the model is missing, attempt a one-time automatic download.
    model_name = "en_core_web_sm"
    if not _ensure_spacy_model(model_name):
        print(
            f"spacy model '{model_name}' is not available and could not be downloaded.\n"
            "Run manually: python -m spacy download en_core_web_sm",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        configuration = {
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": language, "model_name": model_name}],
        }
        provider = NlpEngineProvider(nlp_configuration=configuration)
        nlp_engine = provider.create_engine()
        analyzer = AnalyzerEngine(nlp_engine=nlp_engine)
    except Exception as exc:
        print(f"Failed to initialize AnalyzerEngine: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        raw = analyzer.analyze(
            text=text,
            language=language,
            score_threshold=score_threshold,
        )
    except Exception as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        sys.exit(1)

    findings = []
    for r in sorted(raw, key=lambda x: x.start):
        findings.append(
            {
                "entity_type": r.entity_type,
                "start": r.start,
                "end": r.end,
                "score": round(r.score, 4),
                "excerpt": _excerpt(text, r.start, r.end),
            }
        )
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scan text or a file for PII entities using presidio-analyzer.",
        epilog=(
            "Examples:\n"
            "  # CUDA available:\n"
            "  uv run scripts/pii_scan.py --text 'Call me at +1-555-123-4567'\n"
            "  uv run scripts/pii_scan.py --file src/users.csv\n"
            "\n"
            "  # No CUDA (CPU-only torch):\n"
            "  uv run --extra-index-url https://download.pytorch.org/whl/cpu \\\n"
            "    --with torch scripts/pii_scan.py --file data.txt"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", metavar="TEXT", help="Inline text to scan.")
    group.add_argument("--file", metavar="FILE", help="Path to a text file to scan.")
    parser.add_argument(
        "--language",
        default="en",
        metavar="LANG",
        help="Language code for NLP analysis (default: en).",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        metavar="SCORE",
        help="Minimum confidence score to report, 0–1 (default: 0.5).",
    )
    args = parser.parse_args()

    if args.file:
        path = Path(args.file)
        if not path.exists():
            parser.error(f"File not found: {args.file!r}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(
                f"Cannot read {args.file!r}: binary or non-UTF-8 content.",
                file=sys.stderr,
            )
            sys.exit(1)
        source = args.file
    else:
        text = args.text
        source = "<inline-text>"

    findings = _scan(text, args.language, args.threshold)

    print(
        json.dumps(
            {
                "source": source,
                "language": args.language,
                "score_threshold": args.threshold,
                "finding_count": len(findings),
                "findings": findings,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
