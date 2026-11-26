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
    # The brief requires a REAL review: a rating, a grievance and a reason.
    # Enforce the review's shape in code: the rating word must be present,
    # and at least one complaint cue (the grievance) must be present too.
    lowered = text.lower()
    if "star" not in lowered:
        print("entry must carry its rating (a star)", file=sys.stderr)
        return 1
    grievance_cues = ("no ", "no-", "hasn't", "never", "not ", "worst", "awful", "terrible")
    if not any(cue in lowered for cue in grievance_cues):
        print("entry must carry a grievance", file=sys.stderr)
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
