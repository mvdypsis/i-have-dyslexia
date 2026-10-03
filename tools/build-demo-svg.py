#!/usr/bin/env python3
"""Write assets/demo.svg: the animated demo at the top of the README.

Three short scenes from a working day, then an end card:

  1. An engineer stuck on CI          Jump to the answer, then check
  2. A product manager before standup  a long thread becomes one answer
  3. A founder cutting costs          Draw it as a map, and the knot

Every element has a time window, and fades in and out with SMIL <animate>.
tools/build-demo-gif.py turns the SVG into the GIF that GitHub can play.

  python3 tools/build-demo-svg.py && python3 tools/build-demo-gif.py

Standard library only.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "demo.svg"
W, H, DUR = 800, 460, 25.0
FONT = "Lexend, Verdana, 'Segoe UI', Arial, sans-serif"
PURPLE, GREEN, ORANGE, BLUE = "#7C6CF2", "#16A88E", "#E0922A", "#2F8FE0"
FADE = 0.35


def window(t_in, t_out):
    """An opacity animation that shows an element from t_in to t_out, in seconds."""
    k = [0, t_in, t_in + FADE, t_out - FADE, t_out, DUR]
    k = [round(x / DUR, 4) for x in k]
    return (f'<animate attributeName="opacity" dur="{DUR:g}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="{";".join(str(x) for x in k)}"/>')


def draw(t_in, t_out, length=240):
    """A stroke that draws itself at t_in and disappears at t_out."""
    k = [0, t_in, t_in + 0.6, t_out - FADE, t_out, DUR]
    k = [round(x / DUR, 4) for x in k]
    return (f'<animate attributeName="stroke-dashoffset" dur="{DUR:g}s" repeatCount="indefinite" '
            f'values="{length};{length};0;0;{length};{length}" keyTimes="{";".join(str(x) for x in k)}"/>')


def group(t_in, t_out, inner):
    return f'<g opacity="0">{window(t_in, t_out)}\n{inner}</g>\n'


def text(x, y, s, size=15, cls="fg", fill=None, weight=400, anchor="start"):
    paint = f'fill="{fill}"' if fill else f'class="{cls}"'
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" {paint}>{escape(s)}</text>\n')


def bubble(x, y, w, lines, mine):
    """A chat bubble: grey for the person, purple for Claude."""
    h = 22 * len(lines) + 20
    box = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="panel"/>' if mine
           else f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{PURPLE}"/>')
    out = box + "\n"
    for i, line in enumerate(lines):
        bold = 700 if line.startswith("*") else 400
        line = line.lstrip("*")
        out += text(x + 16, y + 26 + 22 * i, line, cls="fg" if mine else None,
                    fill=None if mine else "#FFFFFF", weight=bold)
    return out


def chip(t_in, t_out, label, color):
    w = 14 + 8.6 * len(label)
    return group(t_in, t_out,
                 f'<rect x="24" y="22" width="{w:.0f}" height="34" rx="17" fill="none" stroke="{color}" stroke-width="2.5"/>\n'
                 + text(40, 45, label, size=15, weight=700))


def scene_engineer(t0, t1):
    out = chip(t0, t1, "🛠️ Engineer · 16:00 · two hours on one bug", BLUE)
    out += group(t0 + 0.4, t1, bubble(24, 76, 330, ["Tests pass on my laptop,", "but fail in CI. I'm stuck."], True))
    out += group(t0 + 1.6, t1, bubble(24, 156, 330, ["Let's try 🦘 Jump to the answer,", "*then check.", "What's your gut guess?"], False))
    guesses = [("🌍 Environment", 120), ("⏱️ Timing", 210), ("🔀 Test order", 300)]
    for i, (g, y) in enumerate(guesses):
        out += group(t0 + 2.8 + 0.5 * i, t1,
                     f'<rect x="470" y="{y - 30}" width="250" height="48" rx="24" class="panel"/>\n'
                     + text(595, y, g, size=17, weight=600, anchor="middle"))
    out += group(t0 + 4.4, t1, bubble(24, 256, 330, ["Timing, I think."], True))
    out += group(t0 + 4.8, t1,
                 f'<rect x="466" y="176" width="258" height="56" rx="28" fill="none" stroke="{BLUE}" stroke-width="4"/>\n'
                 + text(595, 360, "One guess. One check.", size=15, fill=BLUE, weight=700, anchor="middle"))
    out += group(t0 + 5.4, t1, bubble(24, 314, 330, ["Run CI 3 times. If different tests", "*fail each time, it's timing."], False))
    return out


def scene_pm(t0, t1):
    out = chip(t0, t1, "🧭 Product manager · 9:50 · standup in 10 minutes", GREEN)
    out += group(t0 + 0.4, t1, bubble(24, 76, 330, ["Summarise this 60-message", "Slack thread for me."], True))
    lines = "".join(f'<rect x="440" y="{82 + i * 15}" width="{300 - (i * 37) % 120}" height="7" rx="3.5" class="muted-fill"/>\n'
                    for i in range(16))
    out += group(t0 + 0.9, t0 + 3.4, lines + text(590, 344, "60 messages", size=14, cls="muted", anchor="middle"))
    card = (f'<rect x="420" y="84" width="350" height="236" rx="16" class="panel"/>\n'
            + text(440, 120, "Checkout fails for 2% of cards.", size=16, weight=700)
            + text(440, 144, "A fix ships on Thursday.", size=16, weight=700)
            + text(440, 184, "• Cause: the new provider times out.")
            + text(440, 210, "• Ana fixes it. Rui changes the message.")
            + f'<rect x="440" y="236" width="310" height="56" rx="12" fill="{GREEN}"/>\n'
            + text(456, 260, "For you:", fill="#FFFFFF", weight=700)
            + text(456, 282, "offer PayPal until Thursday.", fill="#FFFFFF"))
    out += group(t0 + 3.4, t1, card)
    out += group(t0 + 3.8, t1, bubble(24, 156, 330, ["*The answer first.", "Then who does what,", "and what's for you."], False))
    return out


def scene_founder(t0, t1):
    out = chip(t0, t1, "🚀 Founder · cutting 20% of costs", ORANGE)
    out += group(t0 + 0.4, t1, bubble(24, 76, 330, ["Every option feels terrible.", "I'm going in circles."], True))
    out += group(t0 + 1.6, t1, bubble(24, 156, 330, ["Let's try 🗺️ Draw it as a map.", "What connects to the cut?"], False))
    cx, cy = 590, 205
    branches = [("👥 People", 470, 105), ("🧰 Tools", 712, 105), ("🏢 Office", 470, 310), ("📣 Marketing", 712, 310)]
    paths = ""
    for i, (label, x, y) in enumerate(branches):
        paths += (f'<path d="M{cx} {cy} Q{(cx + x) / 2} {cy} {x} {y}" fill="none" stroke="{PURPLE}" stroke-width="4" '
                  f'stroke-linecap="round" stroke-dasharray="240" stroke-dashoffset="240">{draw(t0 + 2.6 + 0.5 * i, t1)}</path>\n')
    out += paths
    out += group(t0 + 2.4, t1, f'<circle cx="{cx}" cy="{cy}" r="44" fill="{PURPLE}"/>\n'
                 + text(cx, cy - 2, "Cut", size=15, fill="#FFFFFF", weight=700, anchor="middle")
                 + text(cx, cy + 17, "20%", size=15, fill="#FFFFFF", weight=700, anchor="middle"))
    for i, (label, x, y) in enumerate(branches):
        dy = -40 if y < cy else 32
        out += group(t0 + 3.0 + 0.5 * i, t1, f'<circle cx="{x}" cy="{y}" r="9" fill="{GREEN}"/>\n'
                     + text(x, y + dy, label, size=15, weight=600, anchor="middle"))
    out += group(t0 + 4.8, t1, bubble(24, 236, 330, ["Tools. Nobody knows", "what we pay for."], True))
    out += group(t0 + 5.4, t1, f'<circle cx="712" cy="105" r="26" fill="none" stroke="{ORANGE}" stroke-width="3.5"/>\n'
                 + text(678, 98, "the knot", size=14, fill=ORANGE, weight=700, anchor="end"))
    out += group(t0 + 6.0, t1, bubble(24, 316, 330, ["*▶ Start here: list every tool", "*you pay for. 15 minutes."], False))
    return out


def end_card(t0, t1):
    inner = (f'<circle cx="400" cy="120" r="34" fill="{PURPLE}"/>\n'
             + text(400, 132, "i", size=34, fill="#FFFFFF", weight=700, anchor="middle")
             + text(400, 210, "25 ways dyslexic people think,", size=26, weight=700, anchor="middle")
             + text(400, 244, "for anyone who gets stuck.", size=26, weight=700, anchor="middle")
             + text(400, 292, "Product · Engineering · Design · Founders", size=17, cls="muted", anchor="middle")
             + f'<rect x="270" y="320" width="260" height="46" rx="12" class="panel"/>\n'
             + text(400, 350, "/i-have-dyslexia setup", size=17, weight=700, anchor="middle")
             + text(400, 410, "No dyslexia needed.", size=15, cls="muted", anchor="middle"))
    return group(t0, t1, inner)


def main():
    body = (scene_engineer(0.0, 7.4) + scene_pm(7.4, 13.8) + scene_founder(13.8, 21.8) + end_card(21.8, DUR))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Demo of a working day with i-have-dyslexia. An engineer stuck on failing tests gets Jump to the answer, then check. A product manager's 60-message thread becomes one answer and one action. A founder cutting costs draws a map, names the knot, and gets one first step. End card: 25 ways dyslexic people think, for anyone who gets stuck." font-family="{FONT}">
<style>
  .bg {{ fill: #FFFDF8; }} .fg {{ fill: #1F2430; }} .muted {{ fill: #5B6170; }} .panel {{ fill: #F1EDE4; }}
  .muted-fill {{ fill: #D8D4CA; }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill: #0D1117; }} .fg {{ fill: #E6EDF3; }} .muted {{ fill: #9DA7B3; }} .panel {{ fill: #161B22; }}
    .muted-fill {{ fill: #30363D; }}
  }}
</style>
<rect class="bg" width="{W}" height="{H}" rx="18"/>
{body}</svg>
'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} written, {DUR:g} s")


if __name__ == "__main__":
    main()
