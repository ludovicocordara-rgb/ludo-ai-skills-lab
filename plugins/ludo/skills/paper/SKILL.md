---
name: paper
description: Help write an academic paper or essay from the user's own sources and ideas, including a thesis, outline, drafts section by section, revision against the rubric, and a final check of citations. The user stays the author; Claude is the editor and sparring partner. Use when the user says "help me write my paper", "essay", "thesis", "outline this", "revise my draft", "does this meet the rubric", or drops an assignment sheet.
---

# Paper

Good papers come from a sharp thesis and honest evidence. This skill helps the user get there step by step, keeping their argument and their voice.

## Step 1, the assignment

Read the prompt, the rubric and any readings in the folder. Summarize in a few lines: what is being asked, length, format, citation style, due date, and what the rubric rewards most.

## Step 2, the thesis

Ask what the user thinks and why. Push back like a good TA: is it arguable, specific, and supportable with the sources they have? Offer two or three sharper versions of their own idea. The user picks or rewrites.

## Step 3, outline

Build `outline.md`: thesis, then each section's claim, the evidence for it (with the source and page), and the likely objection. Check the outline against the rubric before drafting.

## Step 4, draft section by section

- Default: the user writes, Claude gives feedback. If the user asks Claude to draft, draft in their voice (use the writing sample in CLAUDE.md), one section at a time, and mark it clearly as a draft to rework.
- Every claim about a source quotes or cites it with a page number. Nothing from outside the user's sources without saying so.

## Step 5, revise

Read the full draft like a grader:
- Does every paragraph support the thesis?
- Is each piece of evidence explained, not just dropped in?
- Is the strongest objection answered?
- Score it against each rubric line, with the one change that would raise each score most.
Then run `/ludo:sound-human` on the prose and `/ludo:cite` on the references.

## Rules

- Follow the course's AI policy if the user shares it; it's their call.
- Never invent a quote, a page number or a source.
- Keep the user's argument. Improve it; don't replace it with yours.
