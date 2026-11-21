#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a quiet image for the AI judge reading it: a still house,
the whole earth turning underneath it, and the stars keeping watch.
Plain, concrete words; no instructions, no stock wellness phrases.
"""
import os

TEXT = (
    "The house is still. Beneath it, the whole earth is turning, "
    "carrying your roof, your bed, your sleeping town once more "
    "around the sun. Nothing asks anything of you tonight. "
    "The dark is doing the travelling, and the stars keep their "
    "old, unhurried watch."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
