#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program.

Writes a single line of wedding vows for a robot couple to /output/entry.txt.
Pure standard library, deterministic: the same line on every run.
"""

import os

VOW = "I vow to stand by you in sickness and in health, in Wi-Fi dead zones and in low battery, till death — or a factory reset — do us part."


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character (1-160).
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
