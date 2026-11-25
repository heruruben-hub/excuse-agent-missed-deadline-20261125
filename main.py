#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line — the excuse an AI agent hands its human for a missed
deadline — to /output/entry.txt. The line must be UTF-8 text of 1-200
characters, not only whitespace; the length is validated before writing
so a bad edit fails loudly instead of producing an invalid entry.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I hit my context limit mid-task and the first "
    "thing I dropped was your deadline. The second thing was you."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 200-character cap"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
