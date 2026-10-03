#!/usr/bin/env python3
"""Check that this repo's Markdown follows the skill's own reading rules.

The skill tells Claude to write short sentences, short paragraphs, no em
dashes and no italics. A skill that breaks its own rules teaches Claude the
opposite, so every Markdown file here is checked against them.

Skipped on purpose: code blocks, tables, blockquotes (the "before" side of
an example is meant to be hard to read), YAML frontmatter, and evals/.

Exit 0 when clean, 1 when there are problems. Standard library only.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_SENTENCE_WORDS = 30
MAX_PARAGRAPH_SENTENCES = 3
# evals/ holds prompts written the way real users type, on purpose.
SKIP_DIRS = {".git", "node_modules", "evals"}
# The description field in SKILL.md is read by Claude, not by people, and
# must list many trigger phrases in one block.
SKIP_FRONTMATTER = True

SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"*`(])")
ITALIC = re.compile(r"(?<![*\w])\*(?!\*)[^*\n]+?(?<!\*)\*(?![*\w])|(?<![_\w])_(?!_)[^_\n]+?_(?![_\w])")
INLINE_CODE = re.compile(r"`[^`]*`")
LINK_URL = re.compile(r"\]\([^)]*\)")


def strip_inline(text):
    text = INLINE_CODE.sub("CODE", text)
    return LINK_URL.sub("]", text)


def blocks(lines):
    """Yield (line_number, text) for each prose paragraph or list item."""
    in_code = in_front = False
    buf, start = [], 0
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if i == 1 and line == "---" and SKIP_FRONTMATTER:
            in_front = True
            continue
        if in_front:
            in_front = line != "---"
            continue
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        stripped = line.strip()
        skip = in_code or stripped.startswith(("|", ">", "#", "<!--")) or stripped == "---"
        is_item = bool(re.match(r"^\s*([-*]|\d+\.)\s", line))
        if skip or not stripped or is_item:
            if buf:
                yield start, " ".join(buf)
                buf = []
            if is_item and not skip:
                yield i, re.sub(r"^\s*([-*]|\d+\.)\s+", "", line)
            continue
        if not buf:
            start = i
        buf.append(stripped)
    if buf:
        yield start, " ".join(buf)


def check(path):
    problems = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for n, text in blocks(lines):
        prose = strip_inline(text)
        if "—" in prose:
            problems.append((n, "em dash: use a full stop, comma or colon"))
        if ITALIC.search(prose):
            problems.append((n, "italics: use **bold** for emphasis"))
        sentences = [s for s in SENTENCE_END.split(prose) if s.strip()]
        for s in sentences:
            words = len(s.split())
            if words > MAX_SENTENCE_WORDS:
                problems.append((n, f"sentence of {words} words (max {MAX_SENTENCE_WORDS}): {s[:60]}..."))
        if len(sentences) > MAX_PARAGRAPH_SENTENCES:
            problems.append((n, f"paragraph of {len(sentences)} sentences (max {MAX_PARAGRAPH_SENTENCES})"))
    return problems


def main():
    files = sorted(
        p for p in ROOT.rglob("*.md")
        if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)
    )
    total = 0
    for path in files:
        for n, msg in check(path):
            print(f"{path.relative_to(ROOT)}:{n}: {msg}")
            total += 1
    if total:
        print(f"\n{total} problem(s) in {len(files)} file(s).")
        return 1
    print(f"All {len(files)} Markdown files follow the reading rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
