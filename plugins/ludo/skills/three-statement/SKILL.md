---
name: three-statement
description: Build a linked three-statement financial model (income statement, balance sheet, cash flow statement) in Excel that balances every year, and explain how the statements connect. Use when the user says "three statement model", "3-statement", "financial model", "how do the statements link", "balance sheet doesn't balance", or is learning accounting for finance recruiting.
---

# Three-statement model

The three statements are one system: net income flows to the balance sheet through equity and starts the cash flow statement; the cash flow statement produces the cash on the balance sheet; capex and depreciation move PP&E. When the links are right, the balance sheet balances by itself.

## The ready-made model

This skill ships `scripts/three_statement.py`:
- **Inputs tab** (blue): opening balance sheet, revenue growth by year, gross margin, SG&A, depreciation, capex, receivable, inventory and payable days, interest, tax, debt repayment, dividend payout.
- **Model tab**: base year plus five forecast years of all three statements, every cell a formula, cash coming from the cash flow statement, and a "Check: balances" row that must read OK every year.

```
pip install openpyxl
python3 <this skill's folder>/scripts/three_statement.py model.xlsx                 # sample numbers
python3 <this skill's folder>/scripts/three_statement.py model.xlsx --inputs my.json # a real company
```

## Teaching the links

Walk through one year column, in this order:
1. Revenue down to net income.
2. Net income into equity (minus dividends).
3. Net income to the top of the cash flow statement, plus depreciation, minus increases in working capital.
4. Capex out in investing; debt repaid and dividends out in financing.
5. Net change in cash into the balance sheet's cash line. The check row proves it.

Classic interview question to practice with the model: "Depreciation goes up by $10. Walk me through the three statements." (At a 25% tax rate: net income down $7.50, cash up $2.50, PP&E down $10, equity down $7.50. Balanced.) Change the input and show it.

## If a model doesn't balance

Check, in order: is every balance sheet change on the cash flow statement? Are signs consistent? Does equity roll forward with net income and dividends? Does cash come only from the cash flow statement?
