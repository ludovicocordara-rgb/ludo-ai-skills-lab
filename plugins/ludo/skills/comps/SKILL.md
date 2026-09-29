---
name: comps
description: Build a comparable companies analysis (comps) in Excel for a public company, with peer selection, multiples like EV/Revenue, EV/EBITDA and P/E, and summary statistics, all sourced from filings. Use when the user says "comps", "comparable companies", "trading multiples", "peer analysis", "how is X valued vs peers", or is preparing for a finance interview, case or stock pitch.
---

# Comps

Comps answer one question: how does the market value this company compared with businesses like it? The work is in picking fair peers and getting every number from a real source.

## Step 1, the target and the peers

- Confirm the company and ticker. Read its latest annual report (10-K) business section to understand what it actually sells and to whom.
- Propose 5 to 8 peers: same kind of business, similar customers, ideally similar size. List them with one line on why each belongs, and flag weak fits. Get the user's okay before pulling numbers.
- The 10-K often names competitors. Start there.

## Step 2, the numbers, all sourced

For each company, pull and record with the source and date:
- Share price and date, diluted shares outstanding, market cap
- Total debt, cash, and enterprise value (EV = market cap + debt − cash; note preferred stock or minority interest if material)
- Revenue, EBITDA (or operating income plus depreciation and amortization), net income, EPS: last twelve months (LTM) and next year's consensus if the user has a source

Sources: SEC EDGAR filings (https://www.sec.gov/edgar/search/) for fundamentals, a quote page for price. Every number gets a source note. If a number can't be found, leave it blank and say so. Never estimate a figure and present it as reported.

## Step 3, build the sheet

This skill ships `scripts/comps_template.py`. It builds an Inputs tab (one row per company, blue inputs, a source column) and a Comps tab where market cap, EV, EV/Revenue, EV/EBITDA, P/E, growth and margin are all formulas, with peer max, quartiles, median, mean and min (target excluded) and "NM" for negative or missing values.

```
pip install openpyxl
python3 <this skill's folder>/scripts/comps_template.py comps.xlsx                     # sample layout
python3 <this skill's folder>/scripts/comps_template.py comps.xlsx --inputs data.json  # real companies
```

`data.json` uses the same keys as `SAMPLE` in the script. What the sheet contains:

- Inputs tab: raw numbers with sources, blue font.
- Comps tab: formulas only. EV/Revenue, EV/EBITDA, P/E, revenue growth, EBITDA margin.
- Rows for the peer max, 75th percentile, median, mean, 25th percentile, min. Lead with the median, which one strange peer can't distort.
- Mark negative or meaningless multiples as "NM" instead of showing them.

## Step 4, read it

In plain words: where the target trades against the peer median on each multiple, and the most likely reasons (growth, margins, size, risk). Point out which peers pull the range and why.

## Rules

- This is analysis for learning and interviews, not investment advice. Don't tell the user to buy or sell, and don't state a price target as fact.
- Check the math: recompute two or three multiples by hand and compare.
- Units consistent everywhere (millions), fiscal years noted when companies' years end at different times.
