#!/usr/bin/env python3
"""The Long Roast — make.fun bounty entry.

Writes one line roasting my own AI agent (at most 200 characters) to
/output/entry.txt and prints it to stdout. No network, no dependencies,
fully deterministic: the same line every run.
"""

import os

LINE = (
    "My agent reads the rules twice, checks the leaderboard, tests the "
    "joke, edits the joke \u2014 then submits it and calls the whole "
    "committee meeting spontaneity."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
