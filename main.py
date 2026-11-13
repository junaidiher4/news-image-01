#!/usr/bin/env python3
"""news-image-01 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file (JPEG bytes under the
name entry.png, exactly as the kit prescribes: the format is told apart by
its first bytes, the name stays entry.png either way). The program copies
it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Deterministic: the same bytes, every run. The copy is verified by size
before the program exits, so a partial write fails loudly instead of
leaving a truncated image behind.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
DST = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, DST)
if os.path.getsize(DST) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy incomplete: size mismatch")
