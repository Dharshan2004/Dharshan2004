#!/usr/bin/env python3
"""Draw section headings as SVG, one file per heading.

GitHub strips <style>, style="", class="" and inline <svg> from README
markdown, so the only way to keep a custom mono typeface on a heading is
an <img>. Alt text carries the word for screen readers.

    pip install fonttools brotli
    python scripts/make_headings.py path/to/JetBrainsMono-Bold.ttf
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fontkit import subset_b64  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WIDTH = 880
HEIGHT = 30
SIZE = 13.0
TRACKING = 2.6

HEADINGS = [
    "about",
    "now",
    "work",
    "builds",
    "research",
    "stack",
    "writing",
    "contact",
]


def draw(label, ttf):
    slug = label.replace(" ", "-")
    advance = SIZE * 0.6 + TRACKING
    rule_start = 2 + len(label) * advance + 14
    css = (
        "@font-face{font-family:'JBMH';font-style:normal;font-weight:700;"
        "src:url(data:font/woff2;base64,%s) format('woff2')}"
        ".h{font-family:'JBMH',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;"
        "fill:#1f2328}.r{stroke:#d8dee4}"
        "@media(prefers-color-scheme:dark){.h{fill:#e6edf3}.r{stroke:#2a3138}}"
        % subset_b64(ttf, label)
    )
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d" role="img" aria-label="%s">'
        "<style>%s</style>"
        '<text class="h" x="2" y="20" font-size="%.1f" font-weight="700" '
        'letter-spacing="%.1f">%s</text>'
        '<line class="r" x1="%.1f" y1="15.5" x2="%d" y2="15.5"/>'
        "</svg>"
        % (
            WIDTH,
            HEIGHT,
            WIDTH,
            HEIGHT,
            label,
            css,
            SIZE,
            TRACKING,
            label,
            rule_start,
            WIDTH - 2,
        )
    )
    path = os.path.join(ROOT, "hd-%s.svg" % slug)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(svg)
    print("wrote hd-%-20s %5.1f KB" % (slug + ".svg", os.path.getsize(path) / 1024.0))


if __name__ == "__main__":
    bold = sys.argv[1]
    for heading in HEADINGS:
        draw(heading, bold)
