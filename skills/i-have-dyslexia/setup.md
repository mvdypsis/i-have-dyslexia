# Setup: getting to know the person

The skill knows dyslexia in general. Setup teaches it this one person.
It takes 5 questions and about 3 minutes.

Run it when the person types `/i-have-dyslexia setup`, or asks to set the skill up.

## How to ask

- **One question at a time.** Wait for the answer before the next one.
- **Offer choices**, so the person can answer in a word. Free answers are welcome too.
- **Never correct spelling** in their answers. Take what they meant.
- If they skip a question, move on.

## The 5 questions

1. **Answers.** "How do you like my answers: short, medium, or detailed?"
2. **Pictures.** "When I explain something, do you want a picture first, sometimes, or rarely?"
3. **Thinking.** "What helps you think when you're stuck? For example: drawing a map, a movie or a story, talking it out, or something else."
4. **Writing.** "Which languages do you write in, and which kind: Portugal or Brazil, UK or US?" Then, as a follow-up: "Do you want help with spelling, or just clean versions?"
5. **What gets in the way.** "Is there anything I do that makes things harder? For example: long lists, many questions at once, too much text."

## The profile

Turn the answers into a short profile in the person's own words.

- At most 12 lines. One preference per line, starting with a verb.
- Link to a strategy by name when it fits: "When I'm stuck, use Draw it as a map."

Example:

```
- Keep answers short. Detail only when I ask.
- Show a picture first when you explain something.
- Explain with movie scenes and images.
- When I'm stuck, use Draw it as a map.
- Write Portuguese from Portugal, and UK English.
- Give me clean versions. No spelling lessons.
- Never give me more than 5 bullets.
```

## Saving it

Show the profile and ask: "Shall I save this?" Save only after a yes.

- **In Claude Code:** write it to `~/.claude/i-have-dyslexia/profile.md`. If `CLAUDE_CONFIG_DIR` is set, use that folder instead of `~/.claude`.
- **In the Claude app or claude.ai:** there is no file. Offer to save it to memory, or give it back so they can paste it into their instructions.

Then say, in two lines:

- In Claude Code, the skill now switches on by itself at the start of every session.
- They can change the profile any time by saying "update my profile", and turn it off by deleting the file.

## Updating

When the person says "update my profile", read the file, ask what to change, show the new version, and save it after a yes.
