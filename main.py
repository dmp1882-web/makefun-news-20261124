#!/usr/bin/env python3
"""Entry for make.fun news-image-20261124.

Reproduces the image this repository holds and writes it to
/output/entry.png. The image is stored base64-encoded as entry.png.b64
(plain text, so it travels through text-only file tooling); this program
decodes it back to the exact image bytes. Deterministic, no network,
standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

OUT.parent.mkdir(parents=True, exist_ok=True)
data = base64.b64decode((HERE / "entry.png.b64").read_text(encoding="ascii"))
OUT.write_bytes(data)
