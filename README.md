<p align="center">
  <img src="assets/logo.svg" alt="i-have-dyslexia" width="140" />
</p>

<h1 align="center">i-have-dyslexia</h1>

<p align="center">
  <strong>Dyslexic people spend their lives finding another way.<br/>This skill teaches Claude to do the same.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/mvdypsis/i-have-dyslexia?style=flat" alt="MIT licence"></a>
  <img src="https://img.shields.io/badge/version-0.1.0-7C6CF2?style=flat" alt="Version 0.1.0">
  <img src="https://img.shields.io/badge/built%20by-dyslexic%20thinkers-22C3A6?style=flat" alt="Built by dyslexic thinkers">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/share-how%20you%20think-F2A93B?style=flat" alt="Share how you think"></a>
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

Then say **"I'm dyslexic"**, or type `/i-have-dyslexia`. Say **"stop dyslexia mode"** to turn it off.

Other ways to install, including the Claude app: [INSTALL.md](INSTALL.md).

---

## Two things it does

### 1. Claude thinks like a dyslexic thinker

Many dyslexic people see the big picture, think in pictures, and find paths others miss.
Those strategies are collected here, from dyslexic people, and Claude uses them when **anyone** is stuck.

### 2. Claude works the way dyslexic people say helps

- The answer first, no walls of text.
- No red pen on your spelling.
- Ideas as pictures, and one step at a time.

---

## See the difference

<table>
<tr>
<th width="50%">Without the skill</th>
<th width="50%">With the skill</th>
</tr>
<tr>
<td>

> **"Help me get more people into my bakery. Flyers and Instagram didn't work."**
>
> Here are 12 ideas to grow foot traffic: 1. Run a loyalty program. 2. Partner with local businesses. 3. Host events. 4. Improve your Google listing. 5. Try TikTok. 6. Offer discounts...

</td>
<td>

> Let's try **Find another path**.
>
> Flyers and Instagram both try to reach strangers. The other path: start from the people who already come.
>
> Ask 5 regulars this week: "How did you first find us?"
>
> What do you think they'll say?

</td>
</tr>
<tr>
<td>

> **"why is my build failing"**
>
> The reason the build is failing is because the configuration file that the deployment pipeline relies on, which was updated in the most recent commit, contains a reference to an environment variable that has not yet been defined in the staging environment, so you'll need to add it there before re-running.

</td>
<td>

> **The build fails because a setting is missing in staging.**
>
> 1. The last change added a new setting: `API_KEY`.
> 2. Staging does not have `API_KEY` yet.
> 3. Add `API_KEY` to staging, then run the build again.

</td>
</tr>
<tr>
<td>

> **"fix this for my landlord: the boiler is brokan agian since wenesday"**
>
> Here's the corrected version. Note: "brokan" should be "broken", "agian" should be "again", and "wenesday" should be "Wednesday".

</td>
<td>

> Here's the message:
>
> Hi Mr Santos, the boiler has been broken again since Wednesday, and there's no hot water. Could you send someone this week?

</td>
</tr>
</table>

More pairs in [`examples/`](examples/).

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

## The strategies library

Each strategy is a way dyslexic people think. Claude picks **one**, tells you which, and does it **with** you.

| Strategy | In one line |
|---|---|
| 🗺️ **Draw it as a map** | Put the problem in the middle, and find the knot. |
| 🔭 **Big picture first** | See the whole before the details. |
| 🖼️ **Think in pictures** | Turn the problem into a drawing. |
| 🏁 **Start from the end** | Picture it done, then walk backwards. |
| 🛤️ **Find another path** | When the usual way is blocked, find three others. |
| 🔗 **What is this like?** | Borrow the answer from another area of life. |
| 📖 **Tell it as a story** | Put the facts inside a story people remember. |
| 🗣️ **Talk it out** | Say it before you write it. |
| 🔁 **Repeat until it sticks** | Go over it again, a different way each time. |
| 🎸 **Train it another way** | Practise the weak skill through something you enjoy. |
| 🎭 **Learn by changing roles** | See the problem from inside someone else's job. |

Full steps and examples in [`strategies/`](skills/i-have-dyslexia/strategies/).

**This list is the start, not the end.** The next strategy should be yours. 👇

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
These are the real results for v0.1.0, failures included.

| Test | With | Without |
|---|---|---|
| Stuck: "see it from a different angle" | **1.00** | 0.00 to 0.50 |
| Fix a message, no spelling comments | **1.00** | 0.50 |
| Show a comparison as a picture | **0.75** | 0.50 |
| Summarise a long email | 1.00 | 1.00 |
| Write in European Portuguese | 1.00 | 1.00 |
| Plan my week, with one clear first step | 0.00 | 0.00 |

The skill switched on every time it should. **Planning is the open problem.** Help is welcome.

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

- The strategies are grouped by the six **Dyslexic Thinking** skills named by [Made By Dyslexia](https://www.madebydyslexia.org/): Visualising, Imagining, Communicating, Reasoning, Connecting and Exploring.
- The shape of this repo is inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd).
- Started by [Miguel Vicente](https://github.com/mvdypsis), who is dyslexic. The principles, and the strategies with his name, are his.

## Licence

[MIT](LICENSE). Use it, copy it, change it, share it.

<p align="center">
  ⭐ <b>Star it if Claude found you another path.</b>
</p>
