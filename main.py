"""Roast the Smart Fridge: One Line, Best Laugh Wins.

The entry is a single roast line. This program writes that line, and only
that line, to ``entry.txt`` inside the grader's output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``).

Design:
- One constant line, 119 characters, one sentence fragment chain with two
  turns: the fridge takes "vacation mode" too literally, then the milk
  joins the holiday. Vacation mode is a real smart-fridge feature.
- Deterministic by construction: no randomness, no clock, no network, no
  input. Two runs write byte-identical files.
- Standard library only (``os``, ``pathlib``).
"""

import os
from pathlib import Path

# The roast: 119 characters, a single line.
LINE = (
    "I put my fridge in vacation mode and it took the hint too well \u2014 "
    "it stopped cooling, and now the milk's on holiday too."
)


def main() -> None:
    # Guard the gate at runtime: the sealed scorer only accepts 1-160
    # characters, a single non-blank line. Fail loudly rather than submit
    # an invalid entry if the line is ever edited past the limit.
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"roast line is {len(LINE)} characters, must be 1-160")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("roast line must be one non-blank line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
