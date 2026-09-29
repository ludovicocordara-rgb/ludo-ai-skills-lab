---
name: explain
description: Explain anything (a concept from class, a piece of code, an error message, a file Claude just made, a news story, a term from a meeting) to someone who is new to it, in plain words, building up from what they already know. Use when the user says "explain", "what does this mean", "I don't get it", "ELI5", "walk me through", "what did you just do", or seems lost.
---

# Explain

A good explanation starts where the listener is, not where the expert is. This skill finds that starting point and builds up one step at a time.

## Step 1, find the starting point

If it isn't obvious, ask one quick question: "Have you seen X before, or is this brand new?" Check the user's CLAUDE.md for their major and background, and use examples from their world (an econ major gets supply and demand analogies, an athlete gets training analogies).

## Step 2, explain in layers

1. **One sentence.** What it is and why anyone cares. No jargon.
2. **An everyday comparison** that is actually accurate, then say where the comparison breaks down.
3. **How it really works**, in a few short steps. Introduce each technical term only when needed, and define it right there.
4. **A concrete example** worked all the way through with real numbers or real code.
5. **The common mistake** people make with it.

Stop after the layer that answers the question. Offer the next layer in one line instead of dumping everything.

## For code

- Go top to bottom, in the order the computer runs it, not the order it's written.
- Explain what each part does and why it's there, not just its name.
- Point out the two or three lines that matter most.
- If the user wants to learn, suggest one small change they can make and run to see what happens.

## For errors

Say what the error means in one line, the most likely cause in this specific case, and the fix. Then one line on how to spot it next time.

## Check understanding

End with one short question the user can answer to check they got it, for example "So what would happen if the list were empty?" Only if they want to be quizzed; don't make it homework.
