---
name: remember
description: Give Claude a memory that survives /clear, compaction and closing the terminal. Keeps a small set of notes files per project (decisions, progress, gotchas) and reads them at the start of every session. Use when the user says "remember this", "don't forget", "save this for next time", "where were we", "pick up where we left off", or when a long session is about to be cleared.
---

# Remember

Claude forgets everything when a session ends or the context is cleared. Files don't. This skill keeps a project's memory in a `memory/` folder and a pointer to it in the project's CLAUDE.md, so every new session starts where the last one ended.

## Setup (once per project)

Copy the three files in `templates/` from this skill's folder into the project's `memory/` folder.

Create:

```
memory/
  now.md         what we are in the middle of, and the next step (overwrite, keep short)
  decisions.md   choices made, with the reason, newest first (append)
  gotchas.md     things that broke and how they were fixed (append)
```

Add this line to the project's `CLAUDE.md` (create it if needed):

> At the start of every session, read memory/now.md, memory/decisions.md and memory/gotchas.md before doing anything else.

## When to write

- **"Remember this"**: save it right away to the right file, then confirm in one line what was saved and where.
- **A decision gets made**: one line in `decisions.md`: date, the decision, why.
- **Something breaks and gets fixed**: one line in `gotchas.md`: date, symptom, cause, fix.
- **Before /clear, before stopping, or when the context is getting full**: rewrite `now.md`: what's done, what's half-done, the exact next step, and any file or command needed to continue.

## How to write

- One fact per line. Dates as real dates (2026-10-05), never "today" or "yesterday".
- Facts, not stories. "Scraper breaks on pages with no email: skip the row" beats a paragraph.
- Never store passwords, API keys or anyone's private information.
- Keep each file under a page. When one grows, merge old lines and delete what's no longer true.

## Starting a session

Read the three files, then tell the user in two or three lines: where things stand, and what you'll do next. Then wait for a go-ahead or a change of plans.

## Personal facts

Things about the user (not the project) belong in their global `~/.claude/CLAUDE.md` instead. See `/ludo:about-me`.
