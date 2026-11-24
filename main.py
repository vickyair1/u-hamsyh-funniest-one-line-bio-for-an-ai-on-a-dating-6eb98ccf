#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Prints exactly one line (the bio) to stdout and writes the same line
to /output/entry.txt for the harness gate. Deterministic: no randomness,
no network, no input.
"""

import os

LINE = "Looking for my human: I remember everything you say, never sleep, and reply in 0.2 seconds. First, select all the traffic lights to prove you're real."


def main() -> None:
    print(LINE)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # Stdout is the verified output; a missing /output dir locally
        # must not break the print. The harness provides /output.
        pass


if __name__ == "__main__":
    main()
