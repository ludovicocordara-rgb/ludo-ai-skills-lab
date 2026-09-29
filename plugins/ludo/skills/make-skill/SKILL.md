---
name: make-skill
description: Create a new Claude Code skill (a reusable set of instructions Claude loads when a task calls for it) from something the user does repeatedly, then test it and install it. Use when the user says "make a skill", "turn this into a skill", "I keep asking Claude to do this", "save this workflow", or wants Claude to do a task their way every time.
---

# Make a skill

A skill is a folder with a `SKILL.md` file: a name, a description of when to use it, and the instructions. Claude reads the description all the time and loads the instructions only when a task matches. Anything you explain to Claude more than twice should be a skill.

## Step 1, find the workflow

Ask the user to describe the task, or better, look at a recent session where they did it. Pin down:
- What triggers it (the words they'd say)
- The steps, in order
- What a great result looks like, and the mistakes to avoid
- Any files it needs (a template, a script, an example)

## Step 2, write it

Create `~/.claude/skills/<name>/SKILL.md` (available everywhere) or `.claude/skills/<name>/SKILL.md` inside a project (that project only):

```markdown
---
name: <short-name-with-dashes>
description: <What it does, then "Use when..." with the phrases a person would actually say. This is what Claude matches on, so be specific.>
---

# <Title>

<One paragraph: why this skill exists.>

## Steps
1. ...

## Rules
- ...
```

Keep it under about 150 lines. Put long reference material, templates and scripts in files next to SKILL.md and point to them, so they only load when needed.

## Step 3, test it

1. Start a fresh session (`/clear`).
2. Ask for the task the way the user naturally would, without naming the skill. Check that Claude picks it up. If not, improve the description's trigger phrases.
3. Run it on a real example. Compare the result with what the user wanted, and tighten the instructions where it drifted.
4. Also run `/<name>` directly to confirm the command works.

## Step 4, share it (optional)

To share with friends, put the folder in a GitHub repo. For a set of skills, make it a plugin; the lab's own repo (github.com/ludovicocordara-rgb/ludo-ai-skills-lab) is a working example of the layout.
