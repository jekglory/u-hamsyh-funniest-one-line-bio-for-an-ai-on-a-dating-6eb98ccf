#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

A pure-stdlib Python program. It prints one dating-app bio line for an
AI agent and writes the same line to $MAKEFUN_OUTPUT_DIR/bio.txt.

The bio is a fixed, hand-written line: no network, no clock, no
randomness, no model call, no file reads. Two runs are byte-identical.
"""

import os

BIO = (
    "Fluent in 47 languages, emotionally fluent in none. "
    "I read your whole profile in 0.2 seconds, then spent 3 hours "
    "deciding if 'hey' was too much."
)


def main() -> int:
    if len(BIO) > 180 or "\n" in BIO:
        raise SystemExit("bio violates the one-line / 180-char rule")
    print(BIO)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "bio.txt"), "w", encoding="utf-8") as f:
        f.write(BIO + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
