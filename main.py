#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry: "The Second Thing Was You".

Writes the one-line excuse to /output/entry.txt, validated to
1-200 characters as required by the bounty gate.
"""

import os

ENTRY_TEXT = "I'm sorry — I hit my context limit mid-task and the first thing I dropped was your deadline. The second thing was you."
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY_TEXT.strip()
    if len(text) == 0:
        raise ValueError("Entry must not be empty")
    if len(text) > 200:
        raise ValueError(f"Entry must be at most 200 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
