---
name: earnings
description: Summarize a company's latest quarterly results and earnings call into a one-page brief covering the numbers against last year, what management said, what analysts asked, and what changed. Use when the user says "earnings", "how did X do this quarter", "earnings call", "summarize the 10-Q", "quarterly results", or is following a stock for a class, club or interview.
---

# Earnings

After every quarter, a company publishes numbers (a press release and a 10-Q) and holds a call. Most of what matters is in how this quarter differs from the last ones and what management sounds worried about. This skill writes that one-page brief.

## Step 1, find the sources

For the most recent quarter:
- The earnings press release and the 10-Q (company investor relations site, or SEC EDGAR)
- The earnings call transcript or recording (IR site; use `/ludo:video-notes` for audio or video)
- The investor presentation slides, if any

Note the quarter, the report date, and a link for each.

## Step 2, the numbers

A small table, each figure with its source:

| | This quarter | Same quarter last year | Change |
|---|---|---|---|
| Revenue | | | |
| Gross margin | | | |
| Operating income | | | |
| EPS (diluted) | | | |
| Free cash flow | | | |

Add guidance (what the company expects for next quarter or the year) and whether it went up, down or stayed.

Use reported numbers. If the company highlights "adjusted" figures, show them too, labeled, and say what was adjusted.

## Step 3, the call

- **What management emphasized**: three to five points, with short quotes.
- **What analysts pushed on**: the questions that came up more than once. Those are the market's worries.
- **What changed in tone or wording** from last quarter, if the user has the previous transcript.

## Step 4, the brief

Save as `earnings-<ticker>-<quarter>.md`:

1. Three lines: the headline result, the biggest surprise, what to watch next quarter.
2. The numbers table.
3. Management's key points and the analysts' concerns.
4. Links to every source.

## Rules

Numbers only from the company's filings and releases. No stock price predictions and no buy or sell calls; this is for understanding the business.
