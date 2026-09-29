---
name: equity-note
description: Write a short initiation-style equity research note on a public company, with the business, the key debate, the numbers, a valuation cross-check with comps and DCF, catalysts and risks, all sourced from filings. Use when the user says "research note", "initiation", "equity research", "write up this company", "sell-side style report", or needs a writing sample for finance recruiting.
---

# Equity note

A research note is a structured argument about a company, written for a busy reader. This skill produces a 2 to 3 page note in the standard shape, every number sourced.

## Structure

1. **Headline and summary** (3 to 5 bullets): the view in one line, the key debate, what the market is missing, the catalyst, the main risk.
2. **The business**: what it sells, to whom, how it makes money, segments with revenue share. From the 10-K.
3. **The key debate**: the one or two questions investors argue about, with both sides.
4. **Financials**: a small table of revenue, growth, margins, EPS and free cash flow for the last three years (from filings) and the next two (labeled as the user's estimates, with the assumptions).
5. **Valuation**: `/ludo:comps` for peer multiples, `/ludo:dcf` as a cross-check. Present a range and what you have to believe for each end.
6. **Catalysts**: dated events that could move the debate (earnings dates, product launches, regulatory decisions).
7. **Risks**: three, each with how you'd know early.
8. **Sources**: every filing, transcript and data source with date.

## Method

1. Read the latest 10-K, the last two 10-Qs and the last earnings call (`/ludo:earnings`).
2. Draft the summary last, after the analysis.
3. Keep it tight: short paragraphs, one chart or table per section at most (`/ludo:spreadsheet` or `/ludo:diagram`).
4. Export as a PDF with `/ludo:word-doc` or `/ludo:slides` if the user needs a polished file.

## Rules

Educational writing sample, not investment advice. Frame views as "our thesis" with evidence. No price targets presented as fact. Every figure from a filing or a named source, with its date.
