#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-liner to /output/entry.txt.
Deterministic: fixed string, no randomness, no clock, no network,
stdlib only. The line owns the outage plainly and specifically,
in the voice of the agent that caused it.
"""

import os

LINE = (
    "I shipped untested code to prod on a Friday, nuked checkout "
    "for 40,000 users, and my rollback plan was refreshing the "
    "dashboard. I own it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
