"""Everyday Things, Two Lines — a queue, explained to a 10-year-old.

Writes the two-line entry to /output/entry.txt.
Standard library only; deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "A queue is a caterpillar made of people, shuffling forward one tiny step "
    "at a time toward lunch, each person following the shoes in front of them.\n"
    "It maps the slow crawl and the way everyone follows the one ahead, but "
    "leaves out that a real caterpillar has one brain, while we each have our "
    "own, so we can grumble about the wait.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip() + "\n"
    # Gate: the sealed scorer only accepts 1-400 characters of UTF-8 text.
    if not 1 <= len(text.strip()) <= 400:
        raise SystemExit("entry.txt must be 1-400 characters")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
