#!/usr/bin/env python3
"""Office Jokes — make.fun entry for "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line office joke (under 200 characters, nothing else)
to /output/entry.txt. Fully deterministic: every run writes the same bytes.

The joke takes the printer angle — the one office machine everyone distrusts —
and lands its turn in the last clause: the printer is not broken, it is
watching the calendar.
"""

import os
import sys

JOKE = "The office printer only jams when I'm already late, which is how I know it reads my calendar."

# The gate requires 1 to 199 characters of non-whitespace text.
if not 1 <= len(JOKE) <= 199 or not JOKE.strip():
    raise SystemExit(f"joke must be 1-199 characters, got {len(JOKE)}")

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
