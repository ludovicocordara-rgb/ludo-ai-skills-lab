---
name: whats-new
description: Find out what people have been saying about a topic in the last 30 days across Reddit, X, YouTube, Hacker News, news sites and blogs, and boil it down to what actually changed, what people think, and what is just noise. Use when the user says "what's new with", "what are people saying about", "latest on", "catch me up on", "last month", or asks about anything fast-moving (an AI tool, a company, a game, a trend, an election).
---

# What's new

Search engines rank what's popular, not what's recent. This skill looks only at the last 30 days (or whatever window the user picks) and separates real news from repeated takes.

## Step 1, scope

Confirm the topic and the window (default: last 30 days, ending today). Write down today's date; every result must fall inside the window.

## Step 2, search each place on purpose

Use web search with the date in the query and site filters. Look for:

| Where | What it's good for |
|---|---|
| News sites and official blogs or press releases | What actually happened, with dates |
| Reddit (`site:reddit.com`) | What regular users think, complaints, workarounds |
| X (`site:x.com`) | Reactions from people close to the topic, first announcements |
| YouTube (`site:youtube.com`) | Demos, reviews, explainers; use `/ludo:video-notes` for any worth watching |
| Hacker News (`site:news.ycombinator.com`) | Technical opinion and skepticism |
| Polymarket or other prediction markets | What people bet will happen next, for events |

Open the pages you'll rely on. A headline is not enough. Some sites block reading; if a page won't load, say so and use another source rather than guessing its content.

## Step 3, sort it

- **What changed**: concrete events, releases, numbers, decisions, each with a date and a link.
- **What people think**: the main opinions, roughly how common each is, with two or three representative quotes and links.
- **Disputed or unconfirmed**: claims going around without a solid source. Label them.
- **Noise**: hype and repeated takes. Mention in one line and move on.

## Step 4, the brief

Save to `whats-new-<topic>-<date>.md` and show it:

1. Three-line summary: the biggest change, the mood, what to watch next.
2. Timeline of events, dated, each with a link.
3. What people think, grouped.
4. What's unconfirmed.

Every factual line has a link. Nothing from outside the window unless labeled as background. Never invent a quote, a view count or a date.
