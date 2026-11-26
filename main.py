#!/usr/bin/env python3
"""Deadpan forecast for Nethersfield, a city that does not exist.

Writes one line (127 characters, within the 1-160 gate) to /output/entry.txt.
Deterministic: the text is a constant — no randomness, no clock, no network.
"""

import os

FORECAST = (
    "In Nethersfield, expect drizzle falling upward at 14 degrees, "
    "with a 60% chance your umbrella files a formal complaint by noon."
)


def main() -> None:
    text = FORECAST
    assert 1 <= len(text) <= 160, f"forecast is {len(text)} chars, gate is 1-160"
    assert text.strip(), "forecast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
