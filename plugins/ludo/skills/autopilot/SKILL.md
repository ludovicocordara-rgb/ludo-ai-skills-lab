---
name: autopilot
description: Let Claude work through a whole task list on its own, one item at a time, testing each before ticking it off, until everything is done or it hits something that needs a human. Use when the user says "autopilot", "just build it all", "keep going until it's done", "work through the list", or has a plan.md or task list ready and wants to step away.
---

# Autopilot

Once a project has a clear plan, most of the remaining work doesn't need the user watching. Autopilot runs the plan item by item and only stops for real decisions. It is built to be safe to walk away from.

## Before starting (required)

1. **A written task list.** Use the project's `plan.md` (see `/ludo:plan`). If there isn't one, make it first and get the user's okay. Each item must be small enough to test on its own.
2. **A definition of done** for the whole thing, written in plan.md.
3. **Limits agreed with the user**, multiple choice:
   - How many items before checking in? (recommend: 5)
   - Which model? (recommend Sonnet; autopilot on Opus or Fable uses up Pro limits fast)
   - What Claude may never do alone: delete files outside the project, spend money, send messages or emails, push to GitHub, publish anything. Default: none of these.
4. **Save point**: if the project uses git, commit before starting, so everything can be undone.

## The loop

For each unchecked item, in order:
1. Read `plan.md` and `memory/now.md` (see `/ludo:remember`).
2. Do the item: the smallest change that completes it.
3. **Test it for real**: run it, open the output, check the result. Not just "no errors".
4. If it passes: tick the box, add a line to the Log in plan.md, update `memory/now.md`, commit if using git.
5. If it fails: use `/ludo:fix-it`. After two failed attempts on the same item, stop and report instead of guessing a third time.

## Stop and ask when

- a decision comes up that the plan doesn't answer
- something needs a login, a password, a payment or a message sent
- an item would touch files outside the project
- the check-in count is reached
- usage is getting low

When stopping, say in a few lines: what got done, what's next, and the one question that needs an answer.

## At the end

Test the whole "definition of done" list, then report plainly: what works, what doesn't, what was skipped and why.
