---
name: plan
description: Turn an idea into a written plan in plan.md before any building starts, then keep that file up to date as the work happens so nothing is lost when the session ends or the context fills up. Use when the user says "plan this", "I want to build", "help me start a project", "make a plan.md", or describes a project with more than a few steps.
---

# Plan first

Most failed builds fail before the first line of code: the goal was fuzzy, a key decision was never made, or the plan lived only in a chat that got cleared. This skill puts the plan in a file, `plan.md`, in the project folder. Claude reads it at the start of every session and updates it as work gets done.

## Step 1, discovery

Read what already exists in the folder before asking anything. Then learn enough to picture the finished thing: who uses it, what it does on a normal day, what "done" looks like.

## Step 2, questions, all at once

Ask every open question in one message, as multiple choice, recommended option first, with one line on what each option costs. Include the edge cases you can foresee. Do not trickle questions out during the build.

Good questions are decisions the person can answer without knowing how to code:
- "Should this run on your laptop only, or on a website other people can open?"
- "When the data source is down, should it stop, or skip and keep going?"

## Step 3, write plan.md

Copy `templates/plan.md` from this skill's folder and fill it in. The shape:

```markdown
# <Project name>

## Goal
One or two sentences. What it does and for whom.

## Done means
A short checklist someone could test by hand.

## Decisions
Each choice made in step 2, with the reason in a few words.

## Steps
- [ ] 1. Smallest thing that works end to end
- [ ] 2. ...

## Log
Date, what got done, what broke, what is next.
```

Make step 1 the smallest version that works end to end, even if ugly. Everything after improves it.

## Step 4, build against the plan

- Work one step at a time. Tick the box when it is verified, not when the code is written.
- Add a line to the Log after each step: what changed and anything surprising.
- If a new decision comes up that the plan did not foresee, ask it as multiple choice, record the answer under Decisions, and keep going.

## Step 5, check

When every box is ticked, test the "Done means" list for real and report what passed and what did not. Say plainly what is left.

## Resuming later

At the start of any session in a folder with a plan.md, read it first, then say where things stand in two lines before doing anything else.
