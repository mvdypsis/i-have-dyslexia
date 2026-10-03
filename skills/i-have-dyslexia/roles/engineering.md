---
role: "Engineering"
emoji: "🛠️"
---

# Engineering

Engineers already think in systems and pictures.
These strategies give names to moves that good engineers make, and help when code, docs and tickets turn into walls of text.

## Moments and strategies

| Moment | Strategy | In engineering |
|---|---|---|
| A bug you can't find | Jump to the answer, then check | Name your strongest guess, then the one log line that would prove it |
| A new codebase | Draw it as a map | Map the main modules and the calls between them before reading files |
| Designing a change | Run the movie forward | Trace a request through the system after your change, step by step |
| Choosing between two designs | Build a model | Spike both for an hour, and compare what you learned |
| Stuck for an hour | Talk it out | Explain the problem out loud, line by line, before reading more |
| A ticket that makes no sense | Go and look | Reproduce it yourself, or ask the person who saw it |
| Unknown code or a term | Use the context | Read the callers and the tests around it before the code itself |
| A long design doc to review | Read with your ears | Listen to it once, then read only the parts that matter |
| A system nobody can explain | Tell it as a story | Follow one user request from the click to the database and back |

## How Claude works with an engineer

- Use exact names: files, functions, commands, error messages.
- Show the command or the change first, the explanation second.
- Draw systems as diagrams, with labeled arrows.
- One debugging step at a time, and say what the result means before the next.

## Example

The person says: **"Payments fail sometimes in production and I can't see why"**

Claude answers:

> Let's try Jump to the answer, then check. What's your gut guess: timeouts, bad data, or a race?
> Pick one, and I'll tell you the one log line that would prove it.
