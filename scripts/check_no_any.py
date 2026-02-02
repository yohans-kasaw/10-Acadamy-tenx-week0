#!/usr/bin/env python3
"""Simple check to ensure `Any` isn't used without a `justification:` comment."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE_DIRS = {".venv", "venv", "__pycache__", ".pytest_cache", ".git"}
PATTERN = re.compile(r"\bAny\b")

violations = []

for p in ROOT.rglob("*.py"):
    if any(part in IGNORE_DIRS for part in p.parts):
        continue
    text = p.read_text(encoding="utf8")
    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        if PATTERN.search(line):
            # check same line or up to 2 lines before for justification
            context = "\n".join(lines[max(0, i-3) : i])
            if "justification:" not in context:
                violations.append(f"{p}:{i}: {line.strip()}")

if violations:
    print("Found 'Any' usages without a justification comment:")
    print("\n".join(violations))
    sys.exit(1)
print("OK: No unjustified Any found.")
sys.exit(0)
