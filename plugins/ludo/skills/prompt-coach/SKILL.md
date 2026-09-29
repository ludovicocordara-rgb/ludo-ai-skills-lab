---
name: prompt-coach
description: Turn a vague request into a strong prompt, for Claude or any other AI, by adding the goal, context, constraints, examples and what a good result looks like. Also explains what made it better so the user learns to do it themselves. Use when the user says "improve my prompt", "how should I ask this", "write a prompt for", "why isn't this working", or gets weak results from an AI.
---

# Prompt coach

Most bad AI output comes from a prompt that leaves out what the writer knew but didn't say. This skill fills the gaps and teaches the pattern.

## The pattern

A strong prompt answers six questions:

1. **Goal**: what is this for? ("an email to a professor asking to join her lab")
2. **Context**: who is involved, what's already known, what files or facts matter
3. **Output**: format, length, tone ("under 120 words, plain, one clear ask")
4. **Constraints**: what to avoid, what not to change, what must be true
5. **Example**: a sample of what good looks like, if there is one
6. **Process**: should it ask questions first, plan first, or just go?

## Method

1. Read the user's prompt. Say in one line what the AI would probably do with it as written.
2. Ask only for the missing pieces that matter, multiple choice where possible.
3. Write the improved prompt in a code block, ready to copy.
4. Below it, three bullets max: what changed and why it helps.
5. If it's for Claude Code specifically, suggest what belongs in CLAUDE.md instead (preferences that apply every time) versus in the prompt (this task only).

## Tips worth teaching

- Say what you want, not only what you don't want.
- Give the reason behind a rule; the model generalizes from reasons.
- Ask for a plan first on anything with many steps.
- For a big job, split it into steps and check each one.
- Paste the real thing (the error, the text, the data), not a description of it.
