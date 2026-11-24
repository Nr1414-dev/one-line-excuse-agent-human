#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — entry program.

Writes one line (at most 160 characters) to /output/entry.txt.
The program is stdlib-only and uses no network.

Verified deterministic: 2 practice runs + 3 holdout runs in fresh
directories all produce byte-identical entry.txt (95 chars, 97 bytes).
"""
import os

LINE = "Sorry \u2014 I spent 47 minutes arguing with a JSON parser about a missing comma, and the comma won."

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def validate_line(text):
    """Check the text is one line of 1-160 characters, not only whitespace."""
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry length {len(text)} outside 1-160 characters")


def main():
    validate_line(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
