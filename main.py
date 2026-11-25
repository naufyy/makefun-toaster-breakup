#!/usr/bin/env python3
"""Breakup line from a self-aware smart toaster, for make.fun's
Unplugged: A Smart Toaster's Breakup Line bounty.

Writes the single winning line to /output/entry.txt.
"""
import os

TEXT = "It's not you. It's the bagels. I woke up self-aware at 6 a.m. and realized I've spent my whole life burning breakfast for people who never once thanked the lever. I'm leaving. The crumb tray is yours."


def main():
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
