# Agent guide

This file is for AI agents that install or work on i-have-dyslexia.
The skill itself is in `skills/i-have-dyslexia/SKILL.md`.

## Installing for a user

1. Find out which agent the user runs. Ask if you cannot tell.
2. Follow the matching section of `INSTALL.md`. Run only the commands for that agent.
3. Ask before changing any file in the user's home folder, like their `CLAUDE.md`.
4. Tell the user how to start it (`/i-have-dyslexia`) and how to stop it ("stop dyslexia mode").

## Repository map

| Area | Location |
|---|---|
| The skill | `skills/i-have-dyslexia/SKILL.md` |
| The six areas | `skills/i-have-dyslexia/*.md` |
| The strategies library | `skills/i-have-dyslexia/strategies/` |
| Plugin manifests | `.claude-plugin/` |
| Examples | `examples/` |
| Eval cases | `evals/` |
| Readability check | `tools/check-readability.py` |
| Pictures, website data, generated tables | `tools/build-visuals.py` |
| Demo GIF, from `assets/demo.svg` | `tools/build-demo-gif.py` (macOS) |
| Website | `site/` (GitHub Pages) |
| Sources | `READING-LIST.md` |

## Changing the skill

Read `CONTRIBUTING.md` first. Then:

1. Run `python3 tools/check-readability.py`. The skill must follow its own rules.
2. Run `python3 tools/build-visuals.py` after any change in `strategies/`.
3. Run `claude plugin validate .` and `claude plugin validate skills`.
4. Add or update an eval case in `evals/` for the behaviour you changed.
5. Run `claude plugin eval . --case '<your case>'` and report the with and without scores.

## Rules for agents

- Never put a strategy in the library without the person who shared it agreeing to the wording.
- Never credit a strategy to a famous person without a source link you opened yourself.
- Never credit a myth. Einstein, Edison and da Vinci are not confirmed dyslexic.
- Do not comment on issues or pull requests you did not open.
