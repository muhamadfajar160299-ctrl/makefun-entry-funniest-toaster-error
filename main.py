"""Copy entry.txt byte-identically into $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No temp files: the output is written directly, then its
mode is set to 0644. Fails loudly if the entry is missing or empty.
"""

import os

try:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
except OSError as exc:
    raise SystemExit(f"cannot read entry.txt: {exc}") from exc

if not data.strip():
    raise SystemExit("entry.txt is empty or whitespace-only")

try:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
except KeyError as exc:
    raise SystemExit("MAKEFUN_OUTPUT_DIR is not set") from exc

os.makedirs(out_dir, exist_ok=True)
dst = os.path.join(out_dir, "entry.txt")
with open(dst, "wb") as f:
    f.write(data)
os.chmod(dst, 0o644)
