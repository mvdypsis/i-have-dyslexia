<p align="center">
  <img src="assets/logo.svg" alt="i-have-dyslexia" width="120" />
</p>

<h1 align="center">i-have-dyslexia</h1>

<p align="center">
  <strong>Dyslexic people spend their lives finding another way.<br/>This skill teaches Claude to do the same.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/mvdypsis/i-have-dyslexia?style=flat" alt="MIT licence"></a>
  <img src="https://img.shields.io/badge/version-0.4.1-7C6CF2?style=flat" alt="Version 0.4.1">
  <img src="https://img.shields.io/badge/strategies-25-16A88E?style=flat" alt="25 strategies">
  <a href="https://mvdypsis.github.io/i-have-dyslexia/"><img src="https://img.shields.io/badge/website-find%20your%20strategy-E0922A?style=flat" alt="Find your strategy"></a>
</p>

<p align="center">
  <b>English</b> · <a href="README.pt-PT.md">Português</a>
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Demo of a working day: an engineer stuck on CI gets one guess and one check, a product manager's 60-message thread becomes one answer, and a founder cutting costs draws a map and finds the knot." width="720">
</p>

<p align="center">
  <b>No dyslexia needed.</b> If you get stuck, this is for you too.
</p>

---

## Install in one sentence

Paste this into Claude Code, or any coding agent:

```text
Install the i-have-dyslexia skill/plugin from https://github.com/mvdypsis/i-have-dyslexia, refer to the repo's AGENTS.md for instructions.
```

Then type **`/i-have-dyslexia setup`**. Claude asks you 5 questions, one at a time, and remembers how you like to work.

After that it switches on by itself in every session. Say **"stop dyslexia mode"** to pause it.

Also works in the Claude app, Codex, Gemini CLI and Cursor: see [INSTALL.md](INSTALL.md).

<p align="center">
  <a href="https://mvdypsis.github.io/i-have-dyslexia/"><b>🧭 Not sure where to start? Find your strategy in 10 seconds ➜</b></a>
</p>

---

## Two things it does

### 1. Claude thinks like a dyslexic thinker

Many dyslexic people see the big picture, think in pictures, and find paths others miss.
Those strategies are collected here, from dyslexic people, books and public interviews.
Claude uses them when **anyone** is stuck.

### 2. Claude works the way dyslexic people say helps

- The answer first, no walls of text.
- No red pen on your spelling.
- Ideas as pictures, and one step at a time.

---

## A normal day at work

<table>
<tr>
<th width="50%">Without the skill</th>
<th width="50%">With the skill</th>
</tr>
<tr><td colspan="2"><b>🧭 Product manager, 9:50, standup in 10 minutes</b></td></tr>
<tr>
<td>

> **"Summarise this 60-message Slack thread about the checkout bug"**
>
> The thread begins with a report from support on Monday regarding intermittent failures in the checkout flow, after which several engineers discussed possible causes, including a recent change to the payment provider integration, while the design team raised a separate concern about the error message copy...

</td>
<td>

> **Checkout fails for about 2% of card payments since Monday. A fix ships Thursday.**
>
> - Cause: the new payment provider times out after 10 seconds.
> - Ana owns the fix. Rui is changing the error message.
>
> **For you:** tell support to offer PayPal until Thursday.

</td>
</tr>
<tr><td colspan="2"><b>🛠️ Engineer, 16:00, two hours on the same bug</b></td></tr>
<tr>
<td>

> **"Tests pass locally but fail in CI and I don't know why"**
>
> Here are 10 common causes: 1. Environment variables. 2. Different Node versions. 3. Timezones. 4. Test order. 5. Caching. 6. Network calls. 7. File paths...

</td>
<td>

> Let's try **Jump to the answer, then check**.
>
> What's your gut guess: the environment, the timing, or the order the tests run in?
>
> Pick one, and I'll give you the one command that proves it.

</td>
</tr>
<tr><td colspan="2"><b>🎨 Designer, 11:00, a 30-page research report to read</b></td></tr>
<tr>
<td>

> **"What does this research say about onboarding?"**
>
> The report presents findings from 14 interviews conducted over three weeks. Participants reported a range of experiences, and several themes emerged across the sessions, including uncertainty, time pressure and trust...

</td>
<td>

> Let's **Picture what you read**. Three images hold the report:
>
> 1. 🧭 **A person lost in a mall:** users don't know which step they're on.
> 2. ⏰ **A phone at a bus stop:** most sign up in under 2 minutes, on the go.
> 3. 🔒 **A locked door:** asking for the card at step 2 makes 6 of 14 leave.
>
> Which one do you want to design for first?

</td>
</tr>
<tr><td colspan="2"><b>🚀 Founder, 22:00, the monthly investor update</b></td></tr>
<tr>
<td>

> **"fix this: we closed 3 new clents this month and revenu grew 12%, burn is down, we are hirring a cto"**
>
> Here's the corrected version. Note: "clents" should be "clients", "revenu" should be "revenue", and "hirring" should be "hiring"...

</td>
<td>

> **Update: September**
>
> We closed 3 new clients, and revenue grew 12%. Burn is down. We're hiring a CTO.
>
> Want me to add the numbers in a small table?

</td>
</tr>
</table>

More examples for each role in the [playbooks](skills/i-have-dyslexia/roles/), and the basics in [`examples/`](examples/).

---

## 25 ways dyslexic people think

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/strategy-map-dark.svg">
  <img src="assets/strategy-map-light.svg" alt="Mind map of 25 thinking strategies, grouped under the six Dyslexic Thinking skills." width="100%">
</picture>

Claude picks **one** strategy, tells you which, and does it **with** you.

📥 [Download the map as a PNG](assets/strategy-map.png), to share on LinkedIn, in slides or in a chat.

<details>
<summary><b>See every strategy as a card</b></summary>
<br/>

<!-- cards:start (generated by tools/build-visuals.py, do not edit by hand) -->
<p align="center">
<a href="skills/i-have-dyslexia/strategies/big-picture-first.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/big-picture-first-dark.svg"><img src="assets/cards/big-picture-first-light.svg" alt="Big picture first: See the whole before the details." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/build-a-model.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/build-a-model-dark.svg"><img src="assets/cards/build-a-model-light.svg" alt="Build a model: Make the idea with your hands, then move the pieces." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/draw-it-as-a-map.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/draw-it-as-a-map-dark.svg"><img src="assets/cards/draw-it-as-a-map-light.svg" alt="Draw it as a map: Put the problem in the middle, and find the knot." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/picture-what-you-read.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/picture-what-you-read-dark.svg"><img src="assets/cards/picture-what-you-read-light.svg" alt="Picture what you read: Turn what you read into images, and remember the pictures." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/think-in-pictures.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/think-in-pictures-dark.svg"><img src="assets/cards/think-in-pictures-light.svg" alt="Think in pictures: Turn the problem into a drawing." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/explain-it-with-a-movie.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/explain-it-with-a-movie-dark.svg"><img src="assets/cards/explain-it-with-a-movie-light.svg" alt="Explain it with a movie: Explain a situation through a movie scene everyone can picture." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/name-it-dont-number-it.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/name-it-dont-number-it-dark.svg"><img src="assets/cards/name-it-dont-number-it-light.svg" alt="Name it, don&#x27;t number it: Give things names you can picture, not codes." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/run-the-movie-forward.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/run-the-movie-forward-dark.svg"><img src="assets/cards/run-the-movie-forward-light.svg" alt="Run the movie forward: Play the future in your head, and watch where it breaks." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/keep-the-message-simple.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/keep-the-message-simple-dark.svg"><img src="assets/cards/keep-the-message-simple-light.svg" alt="Keep the message simple: If it takes a page to explain, it isn&#x27;t ready." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/name-what-you-need.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/name-what-you-need-dark.svg"><img src="assets/cards/name-what-you-need-light.svg" alt="Name what you need: Say what helps you, plainly, before it&#x27;s a problem." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/talk-it-out.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/talk-it-out-dark.svg"><img src="assets/cards/talk-it-out-light.svg" alt="Talk it out: Say it before you write it." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/tell-it-as-a-story.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/tell-it-as-a-story-dark.svg"><img src="assets/cards/tell-it-as-a-story-light.svg" alt="Tell it as a story: Put the facts inside a story people remember." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/jump-to-the-answer-then-check.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/jump-to-the-answer-then-check-dark.svg"><img src="assets/cards/jump-to-the-answer-then-check-light.svg" alt="Jump to the answer, then check: Trust the leap to the answer, then prove it step by step." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/repeat-until-it-sticks.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/repeat-until-it-sticks-dark.svg"><img src="assets/cards/repeat-until-it-sticks-light.svg" alt="Repeat until it sticks: Go over it again, a different way each time." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/start-from-the-end.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/start-from-the-end-dark.svg"><img src="assets/cards/start-from-the-end-light.svg" alt="Start from the end: Picture it done, then walk backwards." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/use-the-context.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/use-the-context-dark.svg"><img src="assets/cards/use-the-context-light.svg" alt="Use the context: When a piece is missing, read the whole picture around it." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/build-a-team-around-your-gaps.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/build-a-team-around-your-gaps-dark.svg"><img src="assets/cards/build-a-team-around-your-gaps-light.svg" alt="Build a team around your gaps: Do what you&#x27;re great at. Hand the rest to someone who&#x27;s great at it." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/learn-by-changing-roles.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/learn-by-changing-roles-dark.svg"><img src="assets/cards/learn-by-changing-roles-light.svg" alt="Learn by changing roles: See the problem from inside someone else&#x27;s job." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/learn-from-cases.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/learn-from-cases-dark.svg"><img src="assets/cards/learn-from-cases-light.svg" alt="Learn from cases: Remember a real example, not a rule." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/what-is-this-like.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/what-is-this-like-dark.svg"><img src="assets/cards/what-is-this-like-light.svg" alt="What is this like?: Borrow the answer from another area of life." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/find-another-path.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/find-another-path-dark.svg"><img src="assets/cards/find-another-path-light.svg" alt="Find another path: When the usual way is blocked, find three others." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/go-and-look.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/go-and-look-dark.svg"><img src="assets/cards/go-and-look-light.svg" alt="Go and look: Skip the report. Go where it happens and watch." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/learn-by-doing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/learn-by-doing-dark.svg"><img src="assets/cards/learn-by-doing-light.svg" alt="Learn by doing: Try it first. Read about it only when you&#x27;re stuck." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/read-with-your-ears.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/read-with-your-ears-dark.svg"><img src="assets/cards/read-with-your-ears-light.svg" alt="Read with your ears: If reading is slow, listen instead." width="400"></picture></a>
<a href="skills/i-have-dyslexia/strategies/train-it-another-way.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cards/train-it-another-way-dark.svg"><img src="assets/cards/train-it-another-way-light.svg" alt="Train it another way: Practise the weak skill through something you enjoy." width="400"></picture></a>
</p>
<!-- cards:end -->

</details>

They come from dyslexic people who shared them, and from **[the best dyslexic thinkers and books](READING-LIST.md)**.
IKEA's Ingvar Kamprad, Richard Branson, Charles Schwab, Nobel winner Carol Greider, John Irving, Jamie Oliver, and more.
Every source is linked and checked.

**This map grows.** The empty spaces are for your strategy. 👇

---

## Use it at work

The same strategies, in the words of your job.
Claude reads the playbook for your role and speaks its language.

| Role | For example |
|---|---|
| 🧭 **[Product](skills/i-have-dyslexia/roles/product.md)** | Planning a launch? Run the movie forward: a pre-mortem. |
| 🛠️ **[Engineering](skills/i-have-dyslexia/roles/engineering.md)** | A bug you can't find? Jump to the answer, then check: your strongest guess, and the one log line that proves it. |
| 🎨 **[Design](skills/i-have-dyslexia/roles/design.md)** | A flow that feels wrong? Run the movie forward: walk it as the user, screen by screen. |
| 🚀 **[Founders and leaders](skills/i-have-dyslexia/roles/leadership.md)** | A hard decision? Run the movie forward: play each option six months ahead. |

On the [website](https://mvdypsis.github.io/i-have-dyslexia/#role-product), pick your role to see every moment and its strategy.

---

## Share how you think

A skill does not retrain Claude. It is a set of instructions Claude reads and follows.
So the way to teach Claude is to write down how great dyslexic thinkers work.

<p align="center">
  <a href="https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=share-a-strategy.yml"><b>➜ Share a strategy</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=what-helped.yml">It helped</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=what-did-not-help.yml">It got in the way</a>
</p>

1. You fill in a short form. No code, no git. **Spelling does not matter.**
2. We write it up together, and you check the wording.
3. It joins the library with your name, and Claude uses it to help the next person.

More in [CONTRIBUTING.md](CONTRIBUTING.md).

---


## Try these

Copy any of these into Claude once the skill is on:

| Say this | What happens |
|---|---|
| **"I'm stuck. Draw it as a map."** | Your problem in the middle, the knot found. |
| **"Where am I?"** | A recap card: what's done, and ▶ what's next. |
| **"Break it down."** | Small steps of 15 minutes. Only the next 3 shown. |
| **"Help me write this."** | You say it your way. Claude gives it back clean. |
| **"What does this want from me?"** | A long document becomes the answer, then a to-do list. |
| **"Help me get better."** | Your 3 most common spelling patterns, with a memory trick each. |

---

## The principles

Strategies are what you do. Principles are why you keep going.

When someone fails, feels slow, or wants to give up, Claude uses **one** of these, in one line, then helps with the next step. No speeches.

> **Start from love** · **Do your best** · **Learn to love what you do** · **Be curious** · **Learn from the best** · **Discipline and determination** · **Never give up** · **Balance**

Shared by the founder. Full text in [`principles.md`](skills/i-have-dyslexia/principles.md).

---

## Writing in English and Portuguese

- **The right variety.** Portuguese means Portugal unless you say Brazil. English follows yours, UK or US.
- **Your voice stays.** A quick message stays quick.
- **Get better, if you want.** Ask, and Claude shows your 3 most common patterns. Never a list of every mistake.
- **Your tricky words.** Claude can keep a short list, so it understands you faster.

---

## Does it work?

Every change is tested by running Claude **with and without** the skill on the same requests, using `claude plugin eval`.
These are the real results for v0.4.0, failures included.

| Test | With | Without |
|---|---|---|
| Stuck: "see it from a different angle" | **1.00** | 0.00 |
| Learning: "a different way to approach this" | **1.00** | 0.00 |
| Fix a message, no spelling comments | **1.00** | 0.50 |
| Plan my week, with one clear first step | **0.50 to 1.00** | 0.00 |
| Show a comparison as a picture | **0.75** | 0.50 |
| Summarise a long email | 1.00 | 1.00 |
| Write in European Portuguese | 1.00 | 1.00 |
| Answer short when there is "too much text" | 1.00 | 1.00 |
| Setup asks one question at a time | **1.00** | 0.00 |
| Offers to draft a strategy that worked | **0.50** | 0.00 |
| Engineering: a bug you can't find | **1.00** | 0.00 |
| Design: users drop off in a flow | **1.00** | 0.00 |
| Founders: a hard decision | **1.00** | 0.00 |
| Product: a roadmap with 30 requests | 0.00 | 0.00 |

The skill switched on every time it should.

Planning moves between runs, and the comparison picture is not always small enough.
The product test fails on detail: Claude picks the right strategy, then asks two questions instead of one. Help is welcome.

The test cases are in [`evals/`](evals/). The skill's own text is checked by [`tools/check-readability.py`](tools/check-readability.py), because a skill about clear writing must follow its own rules.

---

## The 10 rules

<details>
<summary><b>How Claude writes for a dyslexic reader</b></summary>
<br/>

1. Answer first.
2. One idea per sentence.
3. Short paragraphs.
4. Plain words.
5. Same thing, same name.
6. Structure that guides the eye.
7. No spelling comments.
8. Offer a picture.
9. End long answers with "In short".
10. Warm, never patronising.

Full text in [SKILL.md](skills/i-have-dyslexia/SKILL.md).
</details>

---

## Questions

<details>
<summary><b>Do I need to be dyslexic?</b></summary>
<br/>
No. The strategies help anyone who is stuck. The reading and writing rules switch on when you say you are dyslexic, or ask for them.
</details>

<details>
<summary><b>Does this train Claude?</b></summary>
<br/>
No. A skill is a set of instructions Claude reads. When the library grows, everyone who updates the skill gets the new strategies.
</details>

<details>
<summary><b>Is anything I write sent to this project?</b></summary>
<br/>
No. The skill runs inside your own Claude. Nothing reaches this repo unless you choose to fill in a form.
</details>

<details>
<summary><b>What if a rule doesn't work for me?</b></summary>
<br/>
Tell Claude, in plain words: "shorter", "no diagrams", "just do it". Your words beat the skill. Then tell us, so the next version is better.
</details>

---

## Credits

- The six **Dyslexic Thinking** skills are named by [Made By Dyslexia](https://www.madebydyslexia.org/).
- Strategies inspired by books and public figures are listed with their sources in [READING-LIST.md](READING-LIST.md).
- The shape of this repo is inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd).
- Started by [Miguel Vicente](https://github.com/mvdypsis), who is dyslexic. The principles, and the strategies with his name, are his.

## Licence

[MIT](LICENSE). Use it, copy it, change it, share it.

<p align="center">
  ⭐ <b>Star it if Claude found you another path.</b>
</p>
