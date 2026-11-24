#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- a review of planet Earth left by an alien
tourist -- to /output/entry.txt. Deterministic: the same bytes on every
run. Standard library only.
"""

import os

LINE = (
    "Came for the oceans, stayed because the locals apologise "
    "to furniture they bump into. Earth: polite, damp, 4/5."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
