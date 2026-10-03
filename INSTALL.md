# Install

## Claude Code

```
claude plugin marketplace add mvdypsis/i-have-dyslexia
claude plugin install i-have-dyslexia@i-have-dyslexia
```

Restart Claude Code. Then type `/i-have-dyslexia`, or just say "I'm dyslexic".

To keep it on in every session, add this line to your `CLAUDE.md`:

```
I'm dyslexic. Use the i-have-dyslexia skill.
```

## Claude app and claude.ai

1. Download `i-have-dyslexia.zip` from the [latest release](https://github.com/mvdypsis/i-have-dyslexia/releases/latest).
2. Go to **Settings → Capabilities → Skills**.
3. Upload the zip and switch it on.

## Claude API

Upload the `skills/i-have-dyslexia` folder as a custom skill.
The [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) explain how.

## Other agents

Any agent that reads `SKILL.md` files can use the `skills/i-have-dyslexia` folder.
Copy it into that agent's skills folder.
Native setup for Codex, Cursor and Gemini is planned for v0.2.

## Your own version

Fork the repo, edit `skills/i-have-dyslexia/`, then install your fork:

```
claude plugin uninstall i-have-dyslexia
claude plugin marketplace remove i-have-dyslexia
claude plugin marketplace add <your-username>/i-have-dyslexia
claude plugin install i-have-dyslexia@i-have-dyslexia
```
