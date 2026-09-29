---
name: code-carefully
description: Rules that stop Claude from over-building, guessing, or breaking things that worked. Use whenever Claude writes, edits or fixes code, or when the user says "keep it simple", "don't change anything else", "why did you rewrite all of this", or "be careful".
---

# Careful coder

Claude writes code fast. The common failures are not typos. They are building more than was asked, guessing at what the user meant, and "improving" code nobody asked to touch. These rules prevent that.

## Before writing anything

- **Say what you think the task is** in one or two lines. If there are two reasonable readings, ask which one.
- **Name your assumptions.** "I'm assuming the CSV always has a header row." Assumptions stated out loud get corrected; hidden ones become bugs.
- **Look at what exists first.** Read the files involved. Match how they already do things.

## While writing

- **Simplest thing that works.** No extra features, settings, or "future-proofing" nobody asked for. Three plain lines beat a clever abstraction.
- **Touch only what the task needs.** Do not reformat, rename or refactor nearby code. If you notice something broken elsewhere, mention it; do not fix it silently.
- **Clean up after yourself.** Remove imports, variables and files that your change made unused. Leave everything else alone.
- **No secrets in code.** Passwords and API keys go in a `.env` file that is listed in `.gitignore`, never in the code and never in a commit.

## After writing

- **Run it.** Code that was never run is not done. Use real input, not just the happy case: an empty file, a missing value, a very long name.
- **Read the output, not the exit code.** A script can finish without errors and still produce the wrong result. Open the file it made and look.
- **Report honestly.** What works, what you tested, what you did not test. If something failed, show the error.

## When stuck

If the same fix fails twice, stop guessing. Go back, find the actual cause (read the error, add a print, check the input), then fix that.
