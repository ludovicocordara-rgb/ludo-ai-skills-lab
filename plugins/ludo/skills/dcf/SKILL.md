---
name: dcf
description: Build a simple, clean discounted cash flow (DCF) model in Excel with a live assumptions tab, a five-year forecast, WACC, terminal value and a sensitivity table, and explain every step. Use when the user says "DCF", "discounted cash flow", "intrinsic value", "value this company", or is learning valuation for class, a club or finance recruiting.
---

# DCF

A DCF says a company is worth the cash it will generate, discounted back to today. The model is simple; the assumptions are everything. So this skill keeps the math transparent and makes every assumption a visible, changeable input.

## Step 1, understand the business

Read the latest 10-K (SEC EDGAR) and the last few years of results. In a few lines: how the company makes money, what drives growth, what drives margins. Every assumption later should connect to this.

## The ready-made model

This skill ships `scripts/dcf_template.py`, which builds a complete, formula-driven workbook: an Inputs tab (blue cells), a DCF tab (3 historical years, 5 forecast years, mid-year discounting, Gordon growth terminal value discounted from the end of year 5), and a Sensitivity tab (value per share across WACC and terminal growth). Every output is a live formula.

```
pip install openpyxl
# if pip says "externally-managed-environment": python3 -m venv .venv, then source .venv/bin/activate (Windows: .venv\Scripts\activate), then pip install again
python3 <this skill's folder>/scripts/dcf_template.py dcf.xlsx                  # sample numbers to learn on
python3 <this skill's folder>/scripts/dcf_template.py dcf.xlsx --inputs my.json  # the real company
```

For a real company, write `my.json` with the same keys as `SAMPLE` in the script, every number from a filing. Then open the file and walk the user through each tab.

## Step 2, assumptions tab (all inputs, blue font)

- Revenue growth for each of the next 5 years
- EBIT margin (or EBITDA margin and D&A as % of revenue)
- Tax rate
- Capital expenditure and change in working capital, as % of revenue
- WACC inputs: risk-free rate, equity risk premium, beta, cost of debt, target debt weight
- Terminal growth rate (usually around long-run inflation, 2% to 3%), or an exit multiple

Next to each input, a one-line reason and its source: "History averaged 8%; management guided mid-single digits (Q2 call, Aug 2026)."

## Step 3, the model (formulas only, see /ludo:spreadsheet)

1. Historical 3 years, then 5 forecast years.
2. Revenue, EBIT, taxes, NOPAT, plus D&A, minus capex, minus change in working capital = unlevered free cash flow.
3. Discount factor for each year at WACC.
4. Terminal value (Gordon growth: FCF × (1+g) / (WACC − g)), discounted back.
5. Enterprise value, minus net debt = equity value, divided by diluted shares = value per share.
6. Sensitivity table: value per share across WACC (rows) and terminal growth (columns).

## Step 4, sanity checks

- Terminal value share of EV: if over about 75%, say so. The answer rests mostly on the far future.
- Implied exit multiple from the terminal value: compare with today's multiples (see `/ludo:comps`).
- Growth and margins versus history: flag anything well above the company's own track record.
- WACC must be above terminal growth, or the formula breaks.

## Step 5, explain

Summarize in plain words: the value range from the sensitivity table, the two assumptions that move it most, and what you'd need to believe for the high and low ends.

## Rules

For learning and interviews, not investment advice. No buy or sell calls. Every historical number sourced. Never present an assumption as a fact.
