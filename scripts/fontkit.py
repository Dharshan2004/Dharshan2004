#!/usr/bin/env python3
"""Subset JetBrains Mono and emit base64 woff2 for inlining into SVG.

An external font URL cannot work in these SVGs: they load through an <img>
tag, and browsers refuse subresource fetches for image documents. A
@font-face with a base64 data URI does work, so every SVG carries its own
copy of exactly the glyphs it uses.

    pip install fonttools brotli
    python scripts/fontkit.py path/to/JetBrainsMono-Regular.ttf [Bold.ttf]
"""
import base64
import io
import os
import sys

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts")

# Same ramp as kpriyadharshan.dev AsciiBanner
RAMP = " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
LATIN = "".join(chr(c) for c in range(0x20, 0x7F))


def subset_b64(ttf_path, text):
    """Return base64 woff2 of ttf_path reduced to the glyphs in text."""
    from fontTools import subset

    out = io.BytesIO()
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = []
    options.hinting = False
    options.desubroutinize = True
    options.notdef_outline = False
    options.drop_tables += ["FFTM"]
    font = subset.load_font(ttf_path, options)
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    subset.save_font(font, out, options)
    font.close()
    return base64.b64encode(out.getvalue()).decode("ascii")


def load(name):
    with open(os.path.join(FONT_DIR, name + ".b64"), encoding="ascii") as fh:
        return fh.read().strip()


def write(name, b64):
    os.makedirs(FONT_DIR, exist_ok=True)
    path = os.path.join(FONT_DIR, name + ".b64")
    with open(path, "w", encoding="ascii") as fh:
        fh.write(b64)
    print("%-14s %6.1f KB" % (name, len(base64.b64decode(b64)) / 1024))


if __name__ == "__main__":
    regular = sys.argv[1]
    bold = sys.argv[2] if len(sys.argv) > 2 else regular.replace("Regular", "Bold")
    write("ramp", subset_b64(regular, RAMP))
    write("mono-regular", subset_b64(regular, LATIN))
    write("mono-bold", subset_b64(bold, LATIN))
