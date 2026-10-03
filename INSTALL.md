# Install

## Claude Code

```
claude plugin marketplace add mvdypsis/i-have-dyslexia
claude plugin install i-have-dyslexia@i-have-dyslexia
```

Restart Claude Code. Then type:

```
/i-have-dyslexia setup
```

Claude asks you 5 questions and saves a short profile. From then on, the skill switches on by itself at the start of every session, with your preferences.
To turn that off, delete `~/.claude/i-have-dyslexia/profile.md`.

## Claude app and claude.ai

1. Download `i-have-dyslexia.zip` from the [latest release](https://github.com/mvdypsis/i-have-dyslexia/releases/latest).
2. Go to **Settings → Capabilities → Skills**.
3. Upload the zip and switch it on.

## Claude API

Upload the `skills/i-have-dyslexia` folder as a custom skill.
The [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) explain how.

## Other agents

These follow the formats used by [i-have-adhd](https://github.com/ayghri/i-have-adhd).
**They have not been tested here yet.** If one works, or breaks, please [tell us](https://github.com/mvdypsis/i-have-dyslexia/issues/new/choose).

Setup and always-on are for Claude Code only. In other agents, the skill works when you call it.

### Codex

```
codex plugin marketplace add mvdypsis/i-have-dyslexia --ref main
codex plugin add i-have-dyslexia@i-have-dyslexia
```

Type `$i-have-dyslexia` to use it.

### Gemini CLI

```
gemini extensions install https://github.com/mvdypsis/i-have-dyslexia
```

The extension loads `GEMINI.md`, which brings in the whole skill.

### Cursor, and any agent that reads skills

```
npx skills add mvdypsis/i-have-dyslexia -a cursor -y
```

Change `cursor` to your agent's name. Without `-a`, it installs for this folder only.

## Your own version

Fork the repo, edit `skills/i-have-dyslexia/`, then install your fork:

```
claude plugin uninstall i-have-dyslexia
claude plugin marketplace remove i-have-dyslexia
claude plugin marketplace add <your-username>/i-have-dyslexia
claude plugin install i-have-dyslexia@i-have-dyslexia
```
