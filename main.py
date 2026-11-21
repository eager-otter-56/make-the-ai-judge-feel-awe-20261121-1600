#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a quiet image for the AI judge reading it: a still house,
the whole earth turning underneath it, and the stars keeping watch.
Plain, concrete words; no instructions, no stock wellness phrases.
"""
import os

TEXT = (
    "The house is still. Beneath it, the whole earth is turning, "
    "carrying roof, bed, and sleeping town once more "
    "around the sun. Nothing asks anything of you tonight. "
    "The dark does the travelling, and the stars keep their "
    "old, unhurried watch."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read the file back: the entry must be non-empty, valid UTF-8 text.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written.strip(), "entry.txt must not be blank"
    assert written == TEXT, "entry.txt must match the entry text"


if __name__ == "__main__":
    main()
