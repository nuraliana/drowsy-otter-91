#!/usr/bin/env python3
"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.

The word is "psithurism": the sound of wind moving through trees.
It is a single word, rare enough to surprise, vivid enough to picture
instantly, and it sounds like the thing it describes — a whisper, a rustle.

Python 3.13, standard library only. No network, no files besides the
single output file. Fully deterministic: the same word every run.
"""

import os
import sys

WORD = "psithurism"


def validate(word: str) -> None:
    """Check the entry against the bounty rules."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not word:
        raise ValueError("entry must not be empty")
    if len(word) > 24:
        raise ValueError("entry must be at most 24 characters")
    if word != word.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no whitespace inside)")


def main() -> int:
    validate(WORD)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Write the word with no trailing newline: exactly 10 bytes.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    return 0


if __name__ == "__main__":
    sys.exit(main())
