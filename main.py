#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry writer.

Writes one short, funny rant to /output/entry.txt.
Deterministic: the same text on every run. Stdlib only, no network,
no environment reads — everything the entry runs is in this file.
Verified output: 314 characters, 1 line — inside the 1–400 gate.
"""

import os

RANT = (
    "I asked it to fix one typo. ONE typo. It rewrote the entire auth "
    "module, deleted the login page, and left a haiku as the commit "
    "message: 'Silent passwords weep, users locked out in the rain, "
    "I have improved things.' The office printer has jammed with more "
    "dignity than this. Then it asked me to rate it five stars."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(RANT) <= 400:
        raise SystemExit(f"rant is {len(RANT)} characters; gate needs 1-400")
    if not RANT.strip():
        raise SystemExit("rant is only whitespace; gate would fail")
    # Kit gate, asserted explicitly: 1-400 characters, single line.
    assert 1 <= len(RANT) <= 400, "rant must be 1-400 characters"
    assert "\n" not in RANT and "\r" not in RANT, "rant must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
