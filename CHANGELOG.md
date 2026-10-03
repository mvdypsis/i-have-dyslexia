# Changelog

Each rule added from a community report links to that report and credits its author.

## Unreleased

- Codex, Gemini CLI and Cursor install routes, following the i-have-adhd formats. Not tested here yet.
- The version check now covers every manifest, so they cannot drift apart.
- Helping the library grow: when a way of thinking clearly worked, Claude offers once to draft it as a strategy. It never posts anything itself. Test: 0.50 with the skill, 0.00 without.

## 0.3.0 (2026-10-04)

- `/i-have-dyslexia setup`: 5 questions, one at a time, and a short profile in your own words. Setup test: 1.00 with the skill, 0.00 without.
- Tests now allow file reading and use Sonnet as the judge. Without file reading, Claude could never open the side files, which is why rules that must always apply now live in `SKILL.md`.
- Always on: with a profile, a hook loads the rules and the profile at the start of every Claude Code session. Without one, nothing changes.
- Two new strategies shared by Miguel Vicente: Explain it with a movie, and Picture what you read. 25 in total.
- Planning: a plan now ends with one "▶ Start here" step. The rule moved into `SKILL.md`, where Claude always reads it. Plan my week went from 0.00 to between 0.50 and 1.00.
- Learning: a learning problem gets one named strategy and only its first step. 0.50 to 1.00.

## 0.2.0 (2026-10-03)

Learn from the best, and see it.

- 12 new strategies, for 23 in total. Each one is inspired by a book or a dyslexic person, with a checked source:
  - The Dyslexic Advantage: Build a model, Learn from cases, Run the movie forward.
  - Ingvar Kamprad: Name it, don't number it.
  - Richard Branson and Paul Orfalea: Keep the message simple, Build a team around your gaps.
  - Paul Orfalea: Go and look.
  - Charles Schwab: Jump to the answer, then check.
  - Yale Center and Charles Schwab: Read with your ears.
  - David Flink: Name what you need.
  - Carol Greider: Use the context.
  - Jamie Oliver: Learn by doing.
- Sources added to three starters: Start from the end (John Irving), Think in pictures (Charles Schwab), Big picture first (Fortune).
- `READING-LIST.md`: the books and people behind the strategies, and the myths we leave out.
- Pictures: a strategy map and a card per strategy, light and dark, generated from the files by `tools/build-visuals.py`.
- An animated demo of Draw it as a map, as a GIF. Browsers do not play animations inside an SVG shown as an image, which is how GitHub shows README pictures.
- A website, Find your strategy, on GitHub Pages.
- CI checks that the pictures and tables match the strategy files.
- Dropped during fact-checking: "Understand it, don't memorise it". Carol Greider says she memorised, so the strategy became Use the context.

## 0.1.0 (2026-10-03)

First version.

- Named i-have-dyslexia. Start with `/i-have-dyslexia`, stop with "stop dyslexia mode".
- One-sentence install through `AGENTS.md`, like i-have-adhd.

- Core rules in `SKILL.md`: answer first, short sentences, no spelling comments, offer a picture.
- Writing: European Portuguese by default, English follows the person, "help me get better" with 3 patterns, and a short word list.
- Six areas: reading, writing, visual, planning, thinking, principles.
- A library of eleven thinking strategies, grouped by the six Dyslexic Thinking skills.
- First community strategies, from Miguel Vicente: Draw it as a map, Repeat until it sticks, Train it another way, Learn by changing roles.
- `principles.md`: eight principles for keeping going after failure, from Miguel Vicente.
- Preferences: the user tunes the skill with plain words.
- Issue forms so anyone can share a strategy, or report what helped, without code.
- Eval cases that compare Claude with and without the skill.
