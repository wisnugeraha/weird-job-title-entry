#!/usr/bin/env python3
"""Weirdest Job Title - one-line entry for make.fun [u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922].

Writes the line to /output/entry.txt exactly once, verifies the bytes, reports the
char count against the cap, exits 0.
Gate: 1..60 chars, non-blank, UTF-8. Judge ranks lines two at a time.
"""
import os
import sys

LINE = """Regional Director of Emotional Support Furniture"""
MAX = 60
OUT = "/output/entry.txt"

def gate(line: str) -> str:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"line failed gate ({len(line)} chars)")
    return line

def emit(line: str, out: str = OUT) -> None:
    line = gate(line)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(line + "\n")

def confirm(out: str = OUT) -> str:
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != gate(LINE):
        sys.exit("confirm failed: disk content differs from LINE")
    return text

def report(out: str = OUT) -> int:
    text = confirm(out)
    print(f"entry ok: {len(text)} chars (cap {MAX})")
    return len(text)

def main() -> None:
    emit(LINE)
    report(OUT)

if __name__ == "__main__":
    main()
