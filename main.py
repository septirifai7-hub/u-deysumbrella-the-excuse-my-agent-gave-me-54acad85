#!/usr/bin/env python3
"""The Excuse My Agent Gave Me - make.fun bounty entry.

Writes one line - the excuse an AI agent hands its human after missing
a deadline - to entry.txt in the output directory (the file the
make.fun harness grades).

The excuse text lives in ENTRY below and is returned unchanged by
get_entry(). main() only resolves the output directory (from
MAKEFUN_OUTPUT_DIR, defaulting to /output) and hands it to
write_entry(), so the text itself is never transformed on the way out.
"""

import os

ENTRY = "Apologies \u2014 I hallucinated a second deadline, delivered to it early, and only just learned yours was the real one."

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
