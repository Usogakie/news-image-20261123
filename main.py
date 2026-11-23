#!/usr/bin/env python3
"""Entry for make.fun news-image-20261123: emit the 1024x1024 news image.

Reads image.jpg next to this file and byte-copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). No network, no clock,
no randomness — the output is a deterministic copy of the source image.
"""

import os
import shutil
from pathlib import Path

JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "image.jpg"
    if not source.is_file():
        print(f"error: source image not found: {source}", flush=True)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"

    shutil.copyfile(source, dest)

    data = dest.read_bytes()
    if len(data) == 0:
        print(f"error: {dest} is empty", flush=True)
        return 1
    if data[:3] != JPEG_MAGIC:
        print(f"error: {dest} is not a JPEG (bad magic bytes)", flush=True)
        return 1

    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
