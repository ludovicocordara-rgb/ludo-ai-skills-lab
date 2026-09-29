---
name: stock-pitch
description: Prepare a stock pitch for a finance club, class or interview, including the business in plain words, a clear thesis, the evidence, the risks, a valuation cross-check and a one-page write-up with slides if needed. Use when the user says "stock pitch", "pitch a stock", "investment thesis", "long or short", "club pitch", or "pitch me a stock" in an interview prep context.
---

# Stock pitch

A good pitch is a sharp argument, not a company overview: what does the market get wrong, why, and what will make it obvious? This skill builds that argument from sources and pressure-tests it before anyone presents it.

## Step 1, the idea

If the user has a company, start there. If not, ask what they know well (an industry, a product they use, a job they've had) and suggest three companies where that knowledge is an edge, one line each.

## Step 2, understand the business

From the latest 10-K and investor materials:
- What it sells, to whom, and how it makes money, in three sentences a friend would understand
- Revenue by segment and what's growing
- Main competitors and what protects the company (or doesn't)

## Step 3, the thesis

State it in one sentence: "The market thinks X, but actually Y, which will become clear when Z." Then two or three supporting points, each with hard evidence and a source: a number from a filing, a trend from data, a quote from management or customers.

A thesis needs a **catalyst** (an event that will prove it, with a rough date) and must be **falsifiable** (what would prove it wrong).

## Step 4, valuation cross-check

Run `/ludo:comps` and, if time allows, `/ludo:dcf`. Show where the stock trades against peers and what the thesis implies. Present a range, not one precise number.

## Step 5, risks

The three things most likely to make the pitch wrong, each with how likely it is and how you'd know early. Include the strongest argument from the other side. Interviewers always ask.

## Step 6, the deliverables

- `pitch.md`: one page: thesis, evidence, catalyst, valuation, risks.
- Optional slides with `/ludo:slides` (5 to 7 slides).
- A 60-second spoken version, and the five hardest questions someone could ask, with short answers.

## Rules

Every number sourced and dated. Educational exercise, not investment advice: frame it as "my thesis", never "you should buy".
