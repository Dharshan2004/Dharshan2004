#!/usr/bin/env python3
"""Draw the kpriyadharshan.dev mountain-ridge ASCII banner as a self-typing SVG.

This is not a face portrait. It reuses the procedural ridge field from
components/site/AsciiBanner.tsx on the personal site: stacked sine ridges,
soft sky grain, and the same glyph ramp.

    pip install fonttools brotli
    python scripts/fontkit.py path/to/JetBrainsMono-Regular.ttf
    python scripts/make_ascii_svg.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fontkit import load  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GLYPHS = " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
COLS = 96
ROWS = 28
# Match AsciiBanner cell/step ratio (cell 8, step 0.62*cell)
CHAR_W = 7.44
FONT_SIZE = 12.0
LINE_H = 14.0
PAD = 12
ROW_DELAY = 0.055
# Freeze a pleasant frame of the animated field
T = 1.85


def sample(x, y, t, columns, rows):
    nx = x / max(columns - 1, 1)
    ny = y / max(rows - 1, 1)
    side = 0.28 + 0.72 * math.pow(max(0, (nx - 0.12) / 0.88), 1.05)
    ridge = (
        0.28
        + 0.18 * math.sin(nx * math.pi * 1.9 + t * 0.24)
        + 0.11 * math.sin(nx * math.pi * 4.8 - t * 0.16)
        + 0.05 * math.sin(nx * math.pi * 10.5 + t * 0.38)
    )
    depth = max(0, (ny - ridge) / (1 - ridge + 0.001))
    sky = 0.06 + 0.09 * math.sin(t * 0.48 + nx * 2.6 + ny * 1.5) * math.sin(nx * math.pi)
    grain = 0.04 * math.sin(t * 1.2 + x * 0.31 + y * 1.65)
    value = min(1, max(0, (depth * 0.96 + sky * (1 - depth * 0.62) + grain) * side))
    return min(len(GLYPHS) - 1, math.floor(value * (len(GLYPHS) - 0.001)))


def to_lines(columns=COLS, rows=ROWS, t=T):
    lines = []
    for y in range(rows):
        chars = []
        for x in range(columns):
            chars.append(GLYPHS[sample(x, y, t, columns, rows)])
        lines.append("".join(chars).rstrip())
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_svg(lines, out_path, cols):
    width = int(cols * CHAR_W + PAD * 2)
    height = int(len(lines) * LINE_H + PAD * 2)
    face = (
        "@font-face{font-family:'JBM';font-style:normal;font-weight:400;"
        "src:url(data:font/woff2;base64,%s) format('woff2')}" % load("ramp")
    )
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d" role="img" '
        'aria-label="ASCII mountain ridge banner">'
        % (width, height, width, height),
        "<style>%s.a{fill:#57606a;font-family:'JBM',ui-monospace,SFMono-Regular,"
        "Menlo,Consolas,monospace}"
        "@media(prefers-color-scheme:dark){.a{fill:#c9d1d9}}</style>" % face,
    ]
    for i, line in enumerate(lines):
        y = PAD + i * LINE_H
        begin = "%.2fs" % (i * ROW_DELAY)
        end = "%.2fs" % ((i + 1) * ROW_DELAY)
        run = max(len(line), 1) * CHAR_W
        # Base width is the final value so non-SMIL renderers (and camo
        # snapshots) still show the ridge. SMIL browsers type it once.
        parts.append(
            '<clipPath id="c%d"><rect x="%d" y="%.1f" height="%.1f" width="%.1f">'
            '<animate attributeName="width" from="0" to="%.1f" begin="%s" '
            'dur="%.2fs" fill="freeze"/></rect></clipPath>'
            % (i, PAD, y, LINE_H, run, run, begin, ROW_DELAY)
        )
        parts.append(
            '<g clip-path="url(#c%d)"><text xml:space="preserve" x="%d" y="%.1f" '
            'class="a" font-size="%.1f">%s</text></g>'
            % (i, PAD, y + 10.4, FONT_SIZE, escape(line))
        )
        parts.append(
            '<rect y="%.1f" width="5" height="11" class="a" opacity="0">'
            '<animate attributeName="x" from="%d" to="%.1f" begin="%s" dur="%.2fs" '
            'fill="freeze"/><set attributeName="opacity" to="0.75" begin="%s"/>'
            '<set attributeName="opacity" to="0" begin="%s"/></rect>'
            % (y + 1.2, PAD, PAD + run, begin, ROW_DELAY, begin, end)
        )
    parts.append("</svg>")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("".join(parts))
    return width, height


def main():
    lines = to_lines()
    print("\n".join(lines))
    out = os.path.join(ROOT, "ascii.svg")
    width, height = build_svg(lines, out, COLS)
    print(
        "\nwrote %s  %d rows, %dx%d, types for %.1fs"
        % (out, len(lines), width, height, len(lines) * ROW_DELAY + ROW_DELAY)
    )


if __name__ == "__main__":
    main()
