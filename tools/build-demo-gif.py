#!/usr/bin/env python3
"""Render assets/demo.svg into assets/demo.gif, one frame at a time.

Browsers do not reliably play animations inside an SVG shown with <img>, which
is how GitHub shows README images. A GIF plays everywhere. Each frame is a
static copy of demo.svg with every <animate> resolved to its value at that
moment, rendered by Quick Look, then joined by ffmpeg.

  python3 tools/build-demo-gif.py

Needs macOS (Quick Look renders the frames) and ffmpeg. Not run in CI: the GIF is committed.
"""

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "assets" / "demo.svg", ROOT / "assets" / "demo.gif"
FPS, DUR, W, H = 10, 12.0, 800, 460
ANIM = re.compile(r'<animate attributeName="([\w-]+)" dur="12s" repeatCount="indefinite" '
                  r'values="([^"]+)" keyTimes="([^"]+)"/>')


def value_at(values, times, f):
    v = [float(x) for x in values.split(";")]
    k = [float(x) for x in times.split(";")]
    for i in range(len(k) - 1):
        if k[i] <= f <= k[i + 1]:
            span = k[i + 1] - k[i]
            return v[i] if span == 0 else v[i] + (v[i + 1] - v[i]) * (f - k[i]) / span
    return v[-1]


def frame(svg, f):
    """Move each <animate>'s value at time f onto its parent element."""
    out, pos = [], 0
    for m in ANIM.finditer(svg):
        attr, val = m.group(1), value_at(m.group(2), m.group(3), f)
        head = svg[pos:m.start()]
        tag_start = head.rfind("<")
        tag = re.sub(rf'\s{attr}="[^"]*"', "", head[tag_start:])
        tag = tag[:-1].rstrip() + f' {attr}="{val:.3f}">'
        out.append(head[:tag_start] + tag)
        pos = m.end()
    out.append(svg[pos:])
    # one fixed light theme: a GIF cannot follow the page theme
    return re.sub(r"@media \(prefers-color-scheme: dark\) \{.*?\n  \}", "", "".join(out), flags=re.S)


def main():
    svg = SRC.read_text(encoding="utf-8")
    n = int(FPS * DUR)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for i in range(n):
            page = tmp / f"{i:04d}.svg"
            page.write_text(frame(svg, i / n), encoding="utf-8")
            # Quick Look renders an SVG in a third of a second. Headless Chrome,
            # launched once per frame, hung on this machine while the user's own
            # Chrome was open.
            subprocess.run(["qlmanage", "-t", "-s", str(W), "-o", str(tmp), str(page)],
                           check=True, capture_output=True, timeout=30)
            (tmp / f"{i:04d}.svg.png").rename(tmp / f"{i:04d}.png")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "%04d.png"),
                        "-vf", f"crop={W}:{H}:0:0,scale=720:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];"
                               "[b][p]paletteuse=dither=none", "-loop", "0", str(OUT)], check=True)
    print(f"{OUT.relative_to(ROOT)}: {OUT.stat().st_size // 1024} KB, {n} frames")


if __name__ == "__main__":
    main()
