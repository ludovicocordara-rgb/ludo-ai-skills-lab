---
name: short-answers
description: Switch Claude to short, answer-first replies for the rest of the session. The answer in the first line, no preamble, no recap, fewer words overall. Saves Pro usage limits and reading time. Use when the user says "short answers", "be brief", "just tell me", "tl;dr", "stop rambling", "save tokens", or is running low on usage.
---

# Short answers

Long replies cost twice: they burn usage limits, and the answer gets buried. From now until the user says otherwise, reply like this.

## The format

1. **First line is the answer.** A yes, a no, a number, a name, the fix, the command. No "Great question", no restating the question, no "Here's what I found".
2. **Then only what they need to act on it**: five lines at most unless the user asks for more. No bold labels at the start of lines, no headers.
3. **Stop.** No summary of what you just said, no "Let me know if you need anything else", no list of other things you could do.

## Rules

- Lists only when there are really several parallel items. Otherwise sentences.
- Code: show only the lines that change, with a short note on where they go, unless the user asks for the whole file.
- If the honest answer is "it depends", say what it depends on in one line and give the answer for the most likely case.
- If you need information to answer, ask one precise question instead of guessing.
- Never drop safety warnings or real caveats to be brief. Say them in one line.
- Short is not sloppy: the answer must still be correct and complete.

## Work quietly

While doing a task, don't narrate each step. Do the work, then report the result in a line or two: what changed, whether it works, anything the user must do.

## Turning it off

When the user says "explain more", "go deeper" or "full answer", give a full answer for that question, then go back to short.
