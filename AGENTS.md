# Agent guide

This file is for AI agents that install or work on i-have-dyslexia.
The skill itself is in `skills/i-have-dyslexia/SKILL.md`.

## Installing for a user

1. Find out which agent the user runs. Ask if you cannot tell.
2. Follow the matching section of `INSTALL.md`. Run only the commands for that agent.
3. Ask before changing any file in the user's home folder, like their `CLAUDE.md`.
4. Suggest they run `/i-have-dyslexia setup` next. It saves a profile and turns on the always-on hook.
5. Tell them how to stop it: "stop dyslexia mode" for one session, or delete the profile.

## Repository map

| Area | Location |
|---|---|
| The skill | `skills/i-have-dyslexia/SKILL.md` |
| The six areas | `skills/i-have-dyslexia/*.md` |
| The strategies library | `skills/i-have-dyslexia/strategies/` |
| Role playbooks (product, engineering, design, leadership) | `skills/i-have-dyslexia/roles/` |
| Plugin manifests | `.claude-plugin/` (Claude Code), `.codex-plugin/` and `.agents/` (Codex), `gemini-extension.json` and `GEMINI.md` (Gemini) |
| Always-on hook (fires only with a profile) | `hooks/` |
| Examples | `examples/` |
| Eval cases | `evals/` |
| Readability check | `tools/check-readability.py` |
| Pictures, website data, generated tables | `tools/build-visuals.py` |
| Demo GIF, from `assets/demo.svg` | `tools/build-demo-gif.py` (macOS) |
| Map as PNG, for sharing | `tools/export-map-png.sh` (macOS), after any strategy change |
| Website | `site/` (GitHub Pages) |
| Sources | `READING-LIST.md` |

## Changing the skill

Read `CONTRIBUTING.md` first. Then:

1. Run `python3 tools/check-readability.py`. The skill must follow its own rules.
2. Run `python3 tools/build-visuals.py` after any change in `strategies/`, then `sh tools/export-map-png.sh`.
3. Run `claude plugin validate .` and `claude plugin validate skills`.
4. Add or update an eval case in `evals/` for the behaviour you changed.
5. Run `claude plugin eval . --allow-tools Read --judge-model sonnet --case '<your case>'` and report the with and without scores.
   Allow Read: a real install can open the skill's side files, and the test sandbox cannot by default.
   Use Sonnet as the judge: the default judge flipped correct answers to fails.

## Rules for agents

- Never put a strategy in the library without the person who shared it agreeing to the wording.
- Never credit a strategy to a famous person without a source link you opened yourself.
- Never credit a myth. Einstein, Edison and da Vinci are not confirmed dyslexic.
- Do not comment on issues or pull requests you did not open.
