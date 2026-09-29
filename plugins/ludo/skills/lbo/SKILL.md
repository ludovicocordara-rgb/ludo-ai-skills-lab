---
name: lbo
description: Build a live leveraged buyout (LBO) model in Excel with sources and uses, a five-year operating model, a debt schedule with a cash sweep, IRR, money multiple and a returns bridge, and explain what drives the returns. Use when the user says "LBO", "leveraged buyout", "private equity model", "paper LBO", "what IRR", or is preparing for private equity or banking recruiting.
---

# LBO

A private equity firm buys a company using mostly borrowed money, uses the company's cash to pay the debt down, and sells it after about five years. The LBO model answers: what return does the firm make, and where does it come from?

## The ready-made model

This skill ships `scripts/lbo_template.py`, a complete formula-driven workbook:
- **Sources and uses**: purchase price, fees, minimum cash, debt raised, sponsor equity.
- **Operating model**: revenue growth and EBITDA margin by year (inputs), D&A, interest, taxes, net income.
- **Debt schedule**: free cash flow sweeps into debt paydown each year; leverage (debt / EBITDA) by year.
- **Returns**: exit value at an exit multiple, equity value, MOIC and IRR, and a bridge showing how much came from EBITDA growth, multiple change and debt paydown, with a check that it adds up.

```
pip install openpyxl
python3 <this skill's folder>/scripts/lbo_template.py lbo.xlsx                 # sample numbers
python3 <this skill's folder>/scripts/lbo_template.py lbo.xlsx --inputs my.json # a real company
```

`my.json` uses the same keys as `SAMPLE` in the script. For a real company, take revenue and EBITDA from the latest filings and label every assumption.

## Walk the user through it

1. Sources and uses: how much is debt versus equity, and why that matters.
2. Each year: where the cash goes (interest, taxes, capex, working capital, then debt).
3. Returns: MOIC and IRR, and the bridge. Which lever did the work?
4. Sensitivities to try by changing blue cells: exit multiple one turn lower, growth two points lower, entry multiple one turn higher.

## Paper LBO (interview practice)

For a mental-math "paper LBO", give the prompt (entry multiple, leverage, growth, exit), let the user solve it by hand, then check it with the model. Rules of thumb: 2x in 5 years is about 15% IRR; 3x in 5 years is about 25%.

## Rules

Learning and interview prep, not investment advice. Real figures cited with source and date. Never present an assumption as fact.
