---
name: morning
description: A two-minute morning brief with today's classes and meetings, deadlines this week, emails that need a reply, and the one thing to do first. Reads Google Calendar and Gmail once they are connected (see the connectors guide). Use when the user says "morning", "brief me", "what's today", "what do I have", "plan my day", or starts the day in Claude.
---

# Morning

## Needs

Google Calendar and Gmail connected to Claude (claude.ai, Settings, Connectors; see `docs/connectors.md` in the lab repo). Without them, ask the user to paste today's schedule and work from that.

## The brief

Keep it on one screen, in this order:

1. **Today**: every calendar event with time and place, and the gaps longer than an hour ("free 1:00 to 3:30").
2. **Due soon**: deadlines in the next 7 days, from the calendar, recent emails from professors or recruiters, and any `plan.md` or tracker in the current folder. Soonest first.
3. **Needs a reply**: at most five emails from real people (not newsletters or notifications) that are unanswered and look like they need something. One line each: who, what they need.
4. **Do first**: one task, the most important thing that fits in the first free block, and why.

## Rules

- Read only. Never send, archive, delete or label anything, and never accept or decline an invite. If the user wants a reply, draft it and show it; they send it.
- Summarize emails in your own words; don't paste private content from other people at length.
- If a connector is missing or fails, say which one and continue with what's available.
- Short. The whole brief should take under two minutes to read.
