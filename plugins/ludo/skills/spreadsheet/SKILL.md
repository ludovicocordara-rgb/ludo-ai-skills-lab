---
name: spreadsheet
description: Build real Excel or Google Sheets files with working formulas, formatting and charts, or clean up and analyze an existing spreadsheet or CSV. Use when the user says "spreadsheet", "Excel", "xlsx", "make a budget", "tracker", "model", "analyze this CSV", "pivot", "chart this data", or drops a .xlsx or .csv file.
---

# Spreadsheet

A spreadsheet is only useful if someone can change an input and watch it update. So this skill writes real formulas, not pasted numbers.

## Tools

Use Python with `openpyxl` (`pip install openpyxl`) to write .xlsx files, and `pandas` (`pip install pandas`) to read and analyze data. Both files open in Excel, Numbers and Google Sheets (File, Import).

## Building a new sheet

1. **Agree on the layout first:** which tabs, which inputs, which outputs. Show it as a short list.
2. **Inputs on their own tab** (or a clearly marked block), in blue text, so users know what they may change.
3. **Formulas, not values.** Every calculated cell is a formula (`=SUM(B2:B13)`, `=B4*(1+Inputs!B2)`), so the sheet stays live. Never compute in Python and paste the result.
4. **Formatting:** bold headers, frozen top row, number formats that match the data (currency, %, dates), column widths that fit, no merged cells except titles.
5. **Checks:** add a small check cell where it makes sense (totals match, percentages sum to 100%) that shows OK or ERROR.
6. **Charts** only when they answer a question. One clear chart beats four.

## Working with an existing file

1. Read it and describe what's there: tabs, columns, row counts, blanks, obvious errors (numbers stored as text, duplicate rows, mixed date formats).
2. Ask before changing anything. Save changes to a new file (`<name>-clean.xlsx`), never over the original.
3. For analysis, answer the user's question in plain words first, then show the table or chart that proves it.

## Verify before handing it over

- Recalculate: open the file with LibreOffice headless or load it back, and check no cell shows `#REF!`, `#DIV/0!`, `#NAME?` or `#VALUE!`.
- Change one input and confirm the outputs move the way they should.
- Tell the user which cells are inputs and what the key formulas do, in two or three lines.
