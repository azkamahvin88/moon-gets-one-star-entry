#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon, max 120 characters.

Writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
validating the hard gate: one line, 1-120 characters, no control characters.
Python standard library only; no network, no model, no randomness.
"""

import os
import sys

ENTRY = "One star. No Wi-Fi, no water, no atmosphere, and the host hasn't replied in 4.5 billion years."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 120):
        print(f"entry must be 1-120 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry contains control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
