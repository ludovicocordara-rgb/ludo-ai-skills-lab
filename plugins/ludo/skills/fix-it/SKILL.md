---
name: fix-it
description: Fix a bug or error properly by finding the real cause before changing any code, instead of guessing and patching. Use when the user says "it's broken", "fix this", "error", "doesn't work", "why is this happening", pastes an error message, or when a fix has already failed once.
---

# Fix it

Guessing at fixes feels fast and wastes hours: each guess changes something, the bug moves, and nobody knows why. This skill finds the cause first. Every fix it makes, it can explain.

## Step 1, see it fail

- Get the exact error message and the exact steps that cause it. Run it yourself and watch it fail.
- If you can't make it fail, you can't know it's fixed. Find the steps first.
- Note what should happen versus what does happen, in one line each.

## Step 2, find where it breaks

- **Read the whole error.** The last line says what; the lines above say where. Find the first line that points to the user's own code.
- **Check what changed.** If it used to work, what changed since: code, input data, a package version, a file moved? `git diff` if the project uses git.
- **Narrow it down.** Print the actual values just before the failure. Check the input is what you think it is (empty file? a header row? text where a number should be?). Cut the problem in half until one line or one input is left.

## Step 3, name the cause

Write the cause in one sentence, like "The scraper crashes because some profile pages have no email, so the code reads a missing value." If you can't write that sentence yet, keep looking. Don't change code yet.

## Step 4, fix the cause

- Change the smallest thing that fixes the cause. Don't rewrite the file.
- Run the original failing steps. It must pass.
- Run the normal case too, to be sure nothing else broke.
- If there's an obvious sibling case (the other missing field, the empty file), check it.

## Step 5, report

In a few lines: what was wrong, why, what you changed, how you tested it.

## If the first fix fails

Stop. Undo it. A fix that didn't work means the cause in step 3 was wrong. Go back to step 2 with what you just learned. Never stack a second guess on top of a failed one.
