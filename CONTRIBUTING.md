# Contributing

Thank you for helping.
You do not need to code. You do not need perfect spelling.

## The easiest way: fill in a form

Pick a form:

- **[Share how you think](https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=share-a-strategy.yml):** a way of thinking or working that works for you. This is the most valuable one.
- **[It helped](https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=what-helped.yml):** Claude did something that worked for you.
- **[It got in the way](https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=what-did-not-help.yml):** Claude did something that made it harder.
- **[I have an idea](https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=idea.yml):** something Claude should do.

A real example is the most useful thing you can share.
Paste what Claude wrote, and say what you wanted instead.
Remove any private information first.

## What happens to your report

1. A maintainer reads it and may ask a question.
2. If it can become a rule, it gets the label `rule-candidate`.
3. Someone opens a pull request with three things:
   - the **rule**, in the right file in `skills/i-have-dyslexia/`,
   - an **example**, in `examples/`,
   - a **test**, in `evals/`.
4. The changelog credits you, and the rule links to your issue.

## How a strategy joins the library

1. You describe it in the form, in your own words.
2. A maintainer writes it up with `strategies/_template.md`, and checks it with you.
3. They run `python3 tools/build-visuals.py`. Your strategy gets its card, its place on the map and its spot on the website.
4. It goes into `skills/i-have-dyslexia/strategies/`, with your name.
5. If it fits one of the starter strategies, your story is added to that file instead.

## A strategy from a book or a public person

You can also suggest a strategy inspired by a book, or by a dyslexic person who has spoken about how they think.

- Use **Inspired by** instead of **Shared by**, with a link to the source.
- The link must load, and must say what the strategy claims.
- No myths: only people whose dyslexia is confirmed in a public source.

## Changing the skill yourself

If you want to edit the files:

1. Fork the repo and make a branch.
2. Change the skill, add an example and add an eval case.
3. Run the readability check:

   ```
   python3 tools/check-readability.py
   ```

4. Open a pull request. Link the issue it comes from.

## Rules for the skill files

The skill must follow its own rules.
The readability check enforces some of them:

- Sentences of 30 words or fewer.
- Paragraphs of 3 sentences or fewer.
- No em dashes. Use a full stop, a comma or a colon.
- No italics for emphasis. Use **bold**.

Two more rules that a script cannot check:

- **Strengths, not deficits.** Dyslexia is a different way of thinking.
- **One rule, one reason.** If you add a rule, say in the pull request who it helped and why.

## Disagreements

Dyslexia is different for everyone. Two people can want opposite things.
When that happens, the rule goes into `preferences.md` as a choice, not into the core rules.
