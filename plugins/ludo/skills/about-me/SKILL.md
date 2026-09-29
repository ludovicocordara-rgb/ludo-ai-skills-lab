---
name: about-me
description: Interview the user and write a CLAUDE.md file that tells Claude who they are, what they study, what they are working toward and how they like to work. Use when someone says "about me", "set me up", "learn about me", "make my CLAUDE.md", "who am I", or starts using Claude Code for the first time and Claude knows nothing about them. Also use to update an existing CLAUDE.md when their situation changes.
---

# About me

Claude starts every session knowing nothing about the person in front of it. A CLAUDE.md file fixes that: Claude reads it at the start of every session, so everything in it shapes every answer. This skill writes that file by interviewing the person, one short round at a time.

## Where the file goes

Ask which one they want, and recommend the first:

1. **Everywhere** (recommended): `~/.claude/CLAUDE.md`. Claude reads it in every folder, on every project.
2. **This folder only**: `./CLAUDE.md`. Only sessions started in this folder see it.

If a CLAUDE.md already exists at that path, read it first. Keep everything the person wrote. Add to it; never silently delete a line.

## The interview

Ask in three rounds. Each round is a handful of questions in one message, each with example answers so nobody stares at a blank. Accept short answers. Skip anything they don't want to share.

**Round 1, who they are**
- Name, and what they want Claude to call them
- School and year, major or likely major
- Classes this semester
- Clubs, teams, jobs, anything that takes real hours each week

**Round 2, what they are working toward**
- One goal for this semester (a grade, an internship, a project, a habit)
- One thing they would build if building were easy
- Where they get stuck most often

**Round 3, how they want Claude to work**
- Short answers or full explanations?
- Should Claude ask questions before starting big tasks, or just go?
- Anything that annoys them in AI writing (the long dash, "delve", fake enthusiasm, bullet points everywhere)
- A sample of their own writing if they have one handy (an email, a paragraph from a paper). This is the single best way to make Claude sound like them.

## Writing the file

Start from `templates/CLAUDE.md` in this skill's folder and fill it with the interview answers.

Keep it under 60 lines. Plain sentences, grouped under four headings:

```markdown
# About me
# What I'm working on
# How to work with me
# How I write
```

Rules for the content:
- Only facts the person gave. Never invent a class, a goal or a preference.
- Turn preferences into instructions Claude can follow: "Ask me before any task that takes more than a few steps", not "I like being asked".
- If they gave a writing sample, describe its traits in one line each (sentence length, formality, words they use) and keep a short excerpt.
- No personal data they did not volunteer: no address, no phone number, no ID numbers.

## After writing

1. Show the whole file and ask what to change. Edit until they are happy.
2. Prove it works. Suggest one question that only makes sense with the file loaded, for example: "Based on what you know about me, what should I build first in this course?" or "Find three professors at my school whose research fits my interests, with links."
3. Tell them the file grows over time: whenever Claude gets something wrong about them, add one line, or type `#` followed by the rule during a session and Claude saves it to memory.
