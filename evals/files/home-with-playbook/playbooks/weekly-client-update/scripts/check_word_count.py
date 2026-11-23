#!/usr/bin/env python3
"""Usage: check_word_count.py <file> [limit]. Exits 1 if over the limit (default 200)."""
import sys
from pathlib import Path

text = Path(sys.argv[1]).read_text()
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 200
count = len(text.split())
print(f"{count} words (limit {limit}): {'PASS' if count <= limit else 'FAIL'}")
sys.exit(0 if count <= limit else 1)
