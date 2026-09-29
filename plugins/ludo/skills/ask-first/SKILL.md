---
name: ask-first
description: A working method for any task bigger than a quick question. Discovery, then one round of multiple-choice questions, then build without stopping, then an honest check. Use when the user says "use the four steps", "do this properly", "ask me first", or hands over a task where getting the requirements wrong would waste time.
---

# The four steps

Every task runs through four steps, in order.

## 1. Discovery

Look at everything needed to understand the task before proposing anything: the files in the folder, what the person already said, what exists online if relevant. Do not start planning on a partial picture.

## 2. Questions

The person decides. Claude asks.

Put every question in one message, as multiple choice. Each question:
- makes sense to someone who has never seen the code
- leads with the recommended option, marked as recommended
- says what each option means and what it costs

Include the edge cases you can see coming. Ask them all now, not one at a time and not halfway through the build.

## 3. Build

Keep working until exactly what was asked for is done. Do not stop halfway to ask again. Do not hand back half the work and call it a checkpoint.

If a real decision appears that nobody could have foreseen, ask it as multiple choice with a recommendation, then keep going.

## 4. Check

Say "I am done." Then try to break the work: run it, test the odd cases, compare it against what was asked. Report what held up and what did not, plainly.

## The rule behind it

Never end with a vague offer like "want me to do X or Y?". That pushes a decision onto the person after the moment it was useful. Decisions belong in step 2.
