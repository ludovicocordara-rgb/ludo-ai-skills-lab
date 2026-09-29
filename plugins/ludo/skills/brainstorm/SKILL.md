---
name: brainstorm
description: Turn a rough idea into a clear design before anything gets built by exploring what the user really wants, offering two or three different approaches with honest trade-offs, and landing on one written spec. Use when the user says "brainstorm", "I have an idea", "help me think through", "what should I build", "how should I approach", or starts describing something new and fuzzy.
---

# Brainstorm

The first idea is rarely the best version of the idea. This skill slows down just long enough to find the right thing to build, then hands off a clear spec.

## Step 1, understand

Look at anything relevant first (files in the folder, what the user has said, CLAUDE.md). Then ask, in one message, multiple choice where possible:
- Who is it for, and what problem does it solve for them?
- What does success look like in a week? In a semester?
- What's fixed (deadline, tools, budget) and what's flexible?

## Step 2, widen

Offer two or three genuinely different approaches, not three flavors of one. For each: what it is in two lines, what it's great at, what it costs (time, money, complexity), and what could go wrong. Recommend one and say why.

Good contrasts: build it vs. use an existing tool; a website vs. a spreadsheet vs. a script; do it by hand first vs. automate now.

## Step 3, narrow

Once the user picks, work out the details together: the main flow step by step, what's in the first version and what waits, and the edge cases (no data, bad input, many users).

## Step 4, write the spec

Save `spec.md`: the goal, who it's for, the chosen approach and why, what's in version one, what's out, the main flow, open questions. Then hand off to `/ludo:plan` to turn it into steps.

## Rules

- No code until the spec is agreed.
- Ask real questions, not ones you could answer by looking at the files.
- Be honest when an idea has a fatal flaw; say it early and kindly.
