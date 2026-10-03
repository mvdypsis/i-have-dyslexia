#!/usr/bin/env python3
"""Build the pictures and the website data from the strategy files.

Every strategy lives in one Markdown file in skills/i-have-dyslexia/strategies/.
This script reads them all and writes:

  assets/strategy-map-light.svg, assets/strategy-map-dark.svg
  assets/cards/<slug>-light.svg, assets/cards/<slug>-dark.svg
  site/strategies.json

The pictures are generated, never drawn by hand, so a new strategy gets its
card and its place on the map just by adding its file.

  python3 tools/build-visuals.py          write everything
  python3 tools/build-visuals.py --check  fail if anything on disk is stale

Standard library only.
"""

import json
import math
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRATEGIES = ROOT / "skills" / "i-have-dyslexia" / "strategies"
ASSETS = ROOT / "assets"
SITE = ROOT / "site"
REPO = "https://github.com/mvdypsis/i-have-dyslexia"

FONT = "Lexend, Verdana, 'Segoe UI', Arial, sans-serif"

# The six Dyslexic Thinking skills named by Made By Dyslexia, in map order.
# Each has a hue that reads on both the light and the dark ground.
SKILLS = {
    "Visualising": "#7C6CF2",
    "Imagining": "#D9579B",
    "Communicating": "#E0922A",
    "Reasoning": "#2F8FE0",
    "Connecting": "#16A88E",
    "Exploring": "#E2683C",
}

THEMES = {
    "light": {"bg": "#FFFDF8", "fg": "#1F2430", "muted": "#5B6170", "line": "#D8D4CA", "panel": "#F4F1EA"},
    "dark": {"bg": "#0D1117", "fg": "#E6EDF3", "muted": "#9DA7B3", "line": "#30363D", "panel": "#161B22"},
}


# --- reading the strategy files -----------------------------------------------------

def field(text, name):
    m = re.search(rf"^\*\*{re.escape(name)}:\*\*\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def plain(md):
    """Markdown to plain text: links keep their words, bold and code lose their marks."""
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"[*`]", "", md)
    return md.strip()


def links(md):
    return [{"text": t, "url": u} for t, u in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", md)]


def read_strategy(path):
    raw = path.read_text(encoding="utf-8")
    front, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.index("\n---", 4)
        for line in raw[4:end].splitlines():
            k, _, v = line.partition(":")
            front[k.strip()] = v.strip().strip('"')
        body = raw[end + 4:]
    name = re.search(r"^# (.+)$", body, re.M).group(1).strip()
    skills = [s.strip() for s in field(body, "Dyslexic Thinking skill").split(",") if s.strip()]
    unknown = [s for s in skills if s not in SKILLS]
    if not skills or unknown:
        sys.exit(f"{path.name}: unknown Dyslexic Thinking skill {unknown or '(none)'}")
    section = body.split("## How Claude uses it", 1)[-1].split("\n## ", 1)[0]
    steps = [plain(s) for s in re.findall(r"^\d+\.\s+(.+)$", section, re.M)]
    shared = field(body, "Shared by")
    inspired = field(body, "Inspired by")
    return {
        "slug": path.stem,
        "name": name,
        "emoji": front.get("emoji", "•"),
        "summary": front.get("summary", ""),
        "skills": skills,
        "moments": [m.strip() for m in front.get("moments", "").split(",") if m.strip()],
        "use_when": plain(field(body, "Use it when")),
        "steps": steps,
        "shared_by": plain(shared),
        # The links go in "sources"; the credit line keeps only the words.
        "inspired_by": plain(re.sub(r"\s*\((?:\[[^\]]+\]\([^)]+\)(?:,\s*)?)+\)", "", inspired)),
        "sources": links(inspired),
        "url": f"{REPO}/blob/main/skills/i-have-dyslexia/strategies/{path.name}",
    }


ROLES = ROOT / "skills" / "i-have-dyslexia" / "roles"


def load_roles(items):
    """Read each role playbook's table: moment, strategy, what it looks like there."""
    by_name = {i["name"].lower(): i["slug"] for i in items}
    roles = []
    order = ["product", "engineering", "design", "leadership"]
    for path in sorted(ROLES.glob("*.md"), key=lambda p: (order.index(p.stem) if p.stem in order else 99, p.stem)):
        raw = path.read_text(encoding="utf-8")
        front = dict(re.findall(r'^(\w+):\s*"?(.*?)"?$', raw.split("\n---", 1)[0], re.M))
        table = raw.split("## Moments and strategies", 1)[-1].split("\n## ", 1)[0]
        rows = []
        for line in table.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 3 or cells[0] in ("Moment", "") or set(cells[0]) <= set("-"):
                continue
            slug = by_name.get(cells[1].lower())
            if not slug:
                sys.exit(f"roles/{path.name}: no strategy called {cells[1]!r}")
            rows.append({"moment": cells[0], "strategy": slug, "example": cells[2]})
        roles.append({"slug": path.stem, "role": front.get("role", path.stem),
                      "emoji": front.get("emoji", ""), "rows": rows})
    return roles


def load():
    items = [read_strategy(p) for p in sorted(STRATEGIES.glob("*.md")) if not p.name.startswith("_")]
    if not items:
        sys.exit("no strategies found")
    return items


# --- drawing helpers ------------------------------------------------------------------

def wrap(text, width):
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        lines.append(line)
    return lines


def svg(w, h, label, inner, theme):
    t = THEMES[theme]
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-label="{escape(label)}" font-family="{FONT}">\n'
        f'<rect width="{w}" height="{h}" rx="18" fill="{t["bg"]}"/>\n{inner}</svg>\n'
    )


def text(x, y, s, size, fill, anchor="start", weight=400):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>\n')


# --- the strategy map -----------------------------------------------------------------

def strategy_map(items, theme):
    """A two-sided mind map: three skills on each side, strategies stacked beside them.

    A radial fan collided once a skill had more than three strategies. Stacking
    leaves vertically on the outer side keeps every label apart however the
    library grows; the canvas just gets taller.
    """
    t = THEMES[theme]
    W, GAP = 1400, 40
    groups = {s: [i for i in items if i["skills"][0] == s] or [{"emoji": "✨", "name": "Yours?", "empty": True}]
              for s in SKILLS}
    left, right = ["Exploring", "Connecting", "Reasoning"], ["Visualising", "Imagining", "Communicating"]
    rows = [max(len(groups[a]), len(groups[b])) for a, b in zip(left, right)]
    heights = [max(n * GAP, 150) for n in rows]
    top, H = 120, 120 + sum(heights) + 60 * 2 + 70
    cx, cy = W / 2, top + (sum(heights) + 120) / 2
    out = [text(cx, 52, "The strategies, by Dyslexic Thinking skill", 26, t["fg"], "middle", 700),
           text(cx, 82, f"{len(items)} strategies · 6 skills · each one a way dyslexic people think",
                15, t["muted"], "middle")]
    y = top
    for r, h in enumerate(heights):
        sy = y + h / 2
        for side, skill in ((-1, left[r]), (1, right[r])):
            color, members = SKILLS[skill], groups[skill]
            sx = cx + side * 190
            lx = cx + side * 345
            out.append(f'<path d="M{cx} {cy} C{cx + side * 90} {cy} {sx - side * 90} {sy} {sx} {sy}" '
                       f'fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/>\n')
            n = len(members)
            for j, item in enumerate(members):
                ly = sy + (j - (n - 1) / 2) * GAP
                empty = item.get("empty")
                out.append(f'<path d="M{sx} {sy} C{(sx + lx) / 2} {sy} {(sx + lx) / 2} {ly} {lx} {ly}" '
                           f'fill="none" stroke="{color}" stroke-width="2.5" opacity="0.8"/>\n')
                out.append(f'<circle cx="{lx}" cy="{ly:.1f}" r="7" fill="{t["bg"] if empty else color}" '
                           f'stroke="{color}" stroke-width="2.5"/>\n')
                out.append(text(lx + side * 14, ly + 6, f'{item["emoji"]} {item["name"]}', 16,
                                t["muted"] if empty else t["fg"], "start" if side > 0 else "end", 600))
            out.append(f'<circle cx="{sx}" cy="{sy}" r="54" fill="{t["bg"]}" stroke="{color}" stroke-width="4"/>\n')
            out.append(text(sx, sy + 5, skill, 13, t["fg"], "middle", 700))
        y += h + 60
    out.append(f'<circle cx="{cx}" cy="{cy}" r="66" fill="#7C6CF2"/>\n')
    out.append(text(cx, cy - 4, "Dyslexic", 17, "#FFFFFF", "middle", 700))
    out.append(text(cx, cy + 18, "Thinking", 17, "#FFFFFF", "middle", 700))
    out.append(text(cx, H - 24, "Skills named by Made By Dyslexia. Strategies shared by dyslexic people "
                    "or inspired by sourced books and interviews.", 13, t["muted"], "middle"))
    label = (f"Mind map of {len(items)} thinking strategies grouped under the six Dyslexic Thinking skills: "
             + "; ".join(f'{s}: {", ".join(i["name"] for i in m)}' for s, m in groups.items()))
    return svg(W, int(H), label, "".join(out), theme)


# --- one card per strategy ------------------------------------------------------------

def card(item, theme):
    t = THEMES[theme]
    W = 640
    color = SKILLS[item["skills"][0]]
    out, y = [], 0
    out.append(f'<clipPath id="c"><rect width="{W}" height="100%" rx="18"/></clipPath>\n'
               f'<rect x="0" y="0" width="10" height="100%" fill="{color}" clip-path="url(#c)"/>\n')
    out.append(text(40, 70, item["emoji"], 44, t["fg"]))
    out.append(text(104, 58, item["name"], 26, t["fg"], weight=700))
    out.append(text(104, 84, " · ".join(item["skills"]), 14, color, weight=700))
    y = 124
    for line in wrap(item["summary"], 52):
        out.append(text(40, y, line, 18, t["fg"], weight=600))
        y += 26
    y += 10
    out.append(text(40, y, "HOW CLAUDE USES IT", 12, t["muted"], weight=700))
    y += 24
    for n, step in enumerate(item["steps"][:3], 1):
        out.append(f'<circle cx="51" cy="{y - 5}" r="11" fill="{color}"/>\n')
        out.append(text(51, y, str(n), 12, "#FFFFFF", "middle", 700))
        for k, line in enumerate(wrap(step, 60)[:2]):
            out.append(text(72, y, line, 15, t["fg"]))
            y += 21
        y += 8
    credit = (f'Inspired by {item["inspired_by"]}' if item["inspired_by"]
              else f'Shared by {item["shared_by"]}')
    y += 6
    out.append(f'<line x1="40" y1="{y - 10}" x2="{W - 40}" y2="{y - 10}" stroke="{t["line"]}"/>\n')
    for line in wrap(credit, 74)[:2]:
        y += 14
        out.append(text(40, y, line, 13, t["muted"]))
        y += 4
    H = y + 24
    label = f'{item["name"]}: {item["summary"]} Steps: ' + " ".join(item["steps"][:3])
    return svg(W, H, label, "".join(out), theme)


# --- generated blocks inside Markdown -------------------------------------------------

THINKING = ROOT / "skills" / "i-have-dyslexia" / "thinking.md"
README = ROOT / "README.md"


def fill(path, name, body):
    """Replace what sits between <!-- name:start ... --> and <!-- name:end -->."""
    raw = path.read_text(encoding="utf-8")
    m = re.search(rf"(<!-- {name}:start[^>]*-->\n)(.*?)(<!-- {name}:end -->)", raw, re.S)
    if not m:
        sys.exit(f"{path.name}: missing <!-- {name}:start --> marker")
    return raw[:m.start(2)] + body + raw[m.end(2):]


def by_skill(items):
    return sorted(items, key=lambda i: (list(SKILLS).index(i["skills"][0]), i["name"]))


def thinking_table(items):
    rows = ["| Strategy | Skill | Use it when | File |", "|---|---|---|---|"]
    for i in by_skill(items):
        rows.append(f'| {i["name"]} | {i["skills"][0]} | {i["use_when"]} | `strategies/{i["slug"]}.md` |')
    return "\n".join(rows) + "\n"


def readme_cards(items):
    cells = []
    for i in by_skill(items):
        base = f"assets/cards/{i['slug']}"
        cells.append(
            f'<a href="skills/i-have-dyslexia/strategies/{i["slug"]}.md"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{base}-dark.svg">'
            f'<img src="{base}-light.svg" alt="{escape(i["name"])}: {escape(i["summary"])}" width="400">'
            f"</picture></a>")
    return "<p align=\"center\">\n" + "\n".join(cells) + "\n</p>\n"


# --- write or check -------------------------------------------------------------------

def outputs(items):
    files = {}
    for theme in THEMES:
        files[ASSETS / f"strategy-map-{theme}.svg"] = strategy_map(items, theme)
        for item in items:
            files[ASSETS / "cards" / f'{item["slug"]}-{theme}.svg'] = card(item, theme)
    files[THINKING] = fill(THINKING, "strategies", thinking_table(items))
    if "<!-- cards:start" in README.read_text(encoding="utf-8"):
        files[README] = fill(README, "cards", readme_cards(items))
    files[SITE / "strategies.json"] = json.dumps(
        {"skills": SKILLS, "strategies": items, "roles": load_roles(items)}, ensure_ascii=False, indent=2) + "\n"
    return files


VERSIONED = [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
             ".codex-plugin/plugin.json", "gemini-extension.json"]


def version_drift():
    """Every manifest must carry the same version as .claude-plugin/plugin.json."""
    found = {}
    for rel in VERSIONED:
        found[rel] = set(re.findall(r'"version":\s*"([^"]+)"', (ROOT / rel).read_text(encoding="utf-8")))
    want = found[VERSIONED[0]]
    return [f"{rel}: version {sorted(v)} differs from {sorted(want)}" for rel, v in found.items() if v != want]


def main():
    check = "--check" in sys.argv
    drift = version_drift()
    for line in drift:
        print(line)
    if drift:
        return 1
    files = outputs(load())
    stale = [p for p, c in files.items() if not p.exists() or p.read_text(encoding="utf-8") != c]
    orphans = [p for p in (ASSETS / "cards").glob("*.svg") if p not in files] if (ASSETS / "cards").exists() else []
    if check:
        for p in stale + orphans:
            print(f"stale: {p.relative_to(ROOT)}")
        if stale or orphans:
            print("Run: python3 tools/build-visuals.py")
            return 1
        print(f"All {len(files)} generated files are up to date.")
        return 0
    for p, c in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(c, encoding="utf-8")
    for p in orphans:
        p.unlink()
    print(f"Wrote {len(files)} files, removed {len(orphans)} orphans.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
