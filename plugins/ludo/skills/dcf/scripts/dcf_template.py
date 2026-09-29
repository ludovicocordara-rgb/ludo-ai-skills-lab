#!/usr/bin/env python3
"""Build a live, formula-driven DCF workbook.

Usage:
  python3 dcf_template.py dcf.xlsx                 # sample inputs, clearly marked, to learn the model
  python3 dcf_template.py dcf.xlsx --inputs a.json # your own inputs (see SAMPLE below for the keys)

Needs: pip install openpyxl
Blue cells are inputs. Everything else is a formula, so changing any input updates the whole model.
"""
import json
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("openpyxl is missing. Run: pip install openpyxl")

SAMPLE = {
    "company": "Sample Co. (made-up numbers, replace with real ones)",
    "units": "$ millions",
    "history_years": [2023, 2024, 2025],
    "history_revenue": [800.0, 880.0, 960.0],
    "history_ebit": [96.0, 110.0, 125.0],
    "growth": [0.09, 0.08, 0.07, 0.06, 0.05],
    "ebit_margin": [0.13, 0.135, 0.14, 0.14, 0.14],
    "tax_rate": 0.23,
    "da_pct": 0.04,
    "capex_pct": 0.05,
    "nwc_pct": 0.01,
    "risk_free": 0.043,
    "equity_premium": 0.055,
    "beta": 1.1,
    "pre_tax_cost_of_debt": 0.06,
    "debt_weight": 0.2,
    "terminal_growth": 0.025,
    "debt": 300.0,
    "cash": 120.0,
    "shares": 50.0,
}

BLUE = Font(color="1F4E9E")
BOLD = Font(bold=True)
TITLE = Font(bold=True, size=14)
INPUT_FILL = PatternFill("solid", fgColor="EEF3FB")
HEAD_FILL = PatternFill("solid", fgColor="F2F2F2")
THIN = Border(bottom=Side(style="thin", color="999999"))
PCT = "0.0%"
NUM = '#,##0.0;(#,##0.0)'
MONEY = '$#,##0.00'


def build(v, out):
    wb = Workbook()

    # ---------------- Inputs ----------------
    ws = wb.active
    ws.title = "Inputs"
    ws["A1"] = f"{v['company']}: DCF inputs"
    ws["A1"].font = TITLE
    ws["A2"] = f"Units: {v['units']}. Blue cells are inputs; change them and every tab updates."
    rows = [
        ("Tax rate", "tax_rate", PCT),
        ("D&A (% of revenue)", "da_pct", PCT),
        ("Capex (% of revenue)", "capex_pct", PCT),
        ("Change in working capital (% of revenue)", "nwc_pct", PCT),
        ("Risk-free rate", "risk_free", PCT),
        ("Equity risk premium", "equity_premium", PCT),
        ("Beta", "beta", "0.00"),
        ("Pre-tax cost of debt", "pre_tax_cost_of_debt", PCT),
        ("Debt weight in capital", "debt_weight", PCT),
        ("Terminal growth rate", "terminal_growth", PCT),
        ("Total debt", "debt", NUM),
        ("Cash", "cash", NUM),
        ("Diluted shares outstanding (millions)", "shares", NUM),
    ]
    names = {}
    for i, (label, key, fmt) in enumerate(rows, start=4):
        ws.cell(i, 1, label)
        c = ws.cell(i, 2, v[key])
        c.font, c.fill, c.number_format = BLUE, INPUT_FILL, fmt
        ws.cell(i, 3, "Source / reason:").font = Font(italic=True, color="888888")
        names[key] = f"Inputs!$B${i}"
    r = 4 + len(rows) + 1
    ws.cell(r, 1, "Forecast year").font = BOLD
    ws.cell(r + 1, 1, "Revenue growth")
    ws.cell(r + 2, 1, "EBIT margin")
    for j in range(5):
        col = 2 + j
        ws.cell(r, col, f"Year {j + 1}").font = BOLD
        g = ws.cell(r + 1, col, v["growth"][j])
        m = ws.cell(r + 2, col, v["ebit_margin"][j])
        for c in (g, m):
            c.font, c.fill, c.number_format = BLUE, INPUT_FILL, PCT
    grow_row, margin_row = r + 1, r + 2
    ws.column_dimensions["A"].width = 42
    for col in "BCDEFG":
        ws.column_dimensions[col].width = 14

    # ---------------- DCF ----------------
    d = wb.create_sheet("DCF")
    d["A1"] = f"{v['company']}: discounted cash flow"
    d["A1"].font = TITLE
    hy = v["history_years"]
    years = hy + [hy[-1] + i for i in range(1, 6)]
    d.cell(3, 1, "Fiscal year").font = BOLD
    for j, y in enumerate(years):
        c = d.cell(3, 2 + j, f"{y}{'A' if j < len(hy) else 'E'}")
        c.font, c.fill, c.alignment = BOLD, HEAD_FILL, Alignment(horizontal="right")
    nh = len(hy)
    labels = ["Revenue", "  growth", "EBIT", "  margin", "Taxes on EBIT", "NOPAT", "+ D&A", "- Capex",
              "- Change in working capital", "Unlevered free cash flow", "Discount year", "Discount factor",
              "PV of free cash flow"]
    for i, lab in enumerate(labels, start=4):
        d.cell(i, 1, lab)
    R = {lab: 4 + i for i, lab in enumerate(labels)}
    for j in range(len(years)):
        col = 2 + j
        L = get_column_letter(col)
        P = get_column_letter(col - 1)
        if j < nh:
            c = d.cell(R["Revenue"], col, v["history_revenue"][j]); c.font = BLUE
            c = d.cell(R["EBIT"], col, v["history_ebit"][j]); c.font = BLUE
            if j:
                d.cell(R["  growth"], col, f"={L}{R['Revenue']}/{P}{R['Revenue']}-1")
            d.cell(R["  margin"], col, f"={L}{R['EBIT']}/{L}{R['Revenue']}")
        else:
            k = j - nh
            gcell = f"Inputs!{get_column_letter(2 + k)}{grow_row}"
            mcell = f"Inputs!{get_column_letter(2 + k)}{margin_row}"
            d.cell(R["Revenue"], col, f"={P}{R['Revenue']}*(1+{gcell})")
            d.cell(R["  growth"], col, f"={gcell}")
            d.cell(R["EBIT"], col, f"={L}{R['Revenue']}*{mcell}")
            d.cell(R["  margin"], col, f"={mcell}")
            d.cell(R["Taxes on EBIT"], col, f"=-{L}{R['EBIT']}*{names['tax_rate']}")
            d.cell(R["NOPAT"], col, f"={L}{R['EBIT']}+{L}{R['Taxes on EBIT']}")
            d.cell(R["+ D&A"], col, f"={L}{R['Revenue']}*{names['da_pct']}")
            d.cell(R["- Capex"], col, f"=-{L}{R['Revenue']}*{names['capex_pct']}")
            d.cell(R["- Change in working capital"], col,
                   f"=-({L}{R['Revenue']}-{P}{R['Revenue']})*{names['nwc_pct']}")
            d.cell(R["Unlevered free cash flow"], col,
                   f"={L}{R['NOPAT']}+{L}{R['+ D&A']}+{L}{R['- Capex']}+{L}{R['- Change in working capital']}")
            d.cell(R["Discount year"], col, k + 0.5)
            d.cell(R["Discount factor"], col, f"=1/(1+$B$22)^{L}{R['Discount year']}")
            d.cell(R["PV of free cash flow"], col, f"={L}{R['Unlevered free cash flow']}*{L}{R['Discount factor']}")
        for lab, rr in R.items():
            cell = d.cell(rr, col)
            cell.number_format = PCT if lab.strip() in ("growth", "margin") else ("0.0000" if lab == "Discount factor" else NUM)
    d.cell(R["Unlevered free cash flow"], 1).font = BOLD
    last = get_column_letter(1 + len(years))
    first_f = get_column_letter(2 + nh)

    # WACC and value (row numbers are fixed so the formulas can reference them)
    tg = names["terminal_growth"]
    end_year = f"({last}{R['Discount year']}+0.5)"  # terminal value sits at the END of the last year
    block = [
        (19, "Cost of equity", f"={names['risk_free']}+{names['beta']}*{names['equity_premium']}", PCT),
        (20, "After-tax cost of debt", f"={names['pre_tax_cost_of_debt']}*(1-{names['tax_rate']})", PCT),
        (21, "WACC", f"=(1-{names['debt_weight']})*B19+{names['debt_weight']}*B20", PCT),
        (22, "WACC used for discounting", "=B21", PCT),
        (23, "PV of forecast cash flows (mid-year)",
         f"=SUM({first_f}{R['PV of free cash flow']}:{last}{R['PV of free cash flow']})", NUM),
        (24, "Terminal value (Gordon growth)", f"={last}{R['Unlevered free cash flow']}*(1+{tg})/(B22-{tg})", NUM),
        (25, "PV of terminal value (end of year 5)", f"=B24/(1+B22)^{end_year}", NUM),
        (26, "Enterprise value", "=B23+B25", NUM),
        (27, "Less: debt", f"=-{names['debt']}", NUM),
        (28, "Plus: cash", f"={names['cash']}", NUM),
        (29, "Equity value", "=B26+B27+B28", NUM),
        (30, "Value per share", f"=B29/{names['shares']}", MONEY),
        (31, "Terminal value as % of EV", "=B25/B26", PCT),
        (32, "Implied exit EV/EBIT multiple", f"=B24/{last}{R['EBIT']}", '0.0"x"'),
    ]
    d.cell(18, 1, "Valuation").font = BOLD
    for row, lab, f, fmt in block:
        d.cell(row, 1, lab)
        c = d.cell(row, 2, f)
        c.number_format = fmt
    for rr in (21, 30):
        d.cell(rr, 1).font = BOLD
        d.cell(rr, 2).font = BOLD
    d["A33"] = "Check: WACC must be above terminal growth"
    d["B33"] = f'=IF(B22>{names["terminal_growth"]},"OK","ERROR")'
    d.column_dimensions["A"].width = 34
    for j in range(len(years)):
        d.column_dimensions[get_column_letter(2 + j)].width = 12

    # ---------------- Sensitivity ----------------
    s = wb.create_sheet("Sensitivity")
    s["A1"] = "Value per share: WACC (rows) vs terminal growth (columns)"
    s["A1"].font = TITLE
    s["A2"] = "Each cell recomputes the value with its own WACC and growth, using the DCF tab's cash flows."
    waccs = [-0.02, -0.01, 0, 0.01, 0.02]
    grows = [-0.01, -0.005, 0, 0.005, 0.01]
    for j, dg in enumerate(grows):
        c = s.cell(4, 2 + j, f"={names['terminal_growth']}+{dg}")
        c.number_format, c.font, c.fill = PCT, BOLD, HEAD_FILL
    fcf = f"DCF!${first_f}${R['Unlevered free cash flow']}:${last}${R['Unlevered free cash flow']}"
    yrs = f"DCF!${first_f}${R['Discount year']}:${last}${R['Discount year']}"
    last_fcf = f"DCF!${last}${R['Unlevered free cash flow']}"
    last_yr = f"DCF!${last}${R['Discount year']}"
    for i, dw in enumerate(waccs):
        rr = 5 + i
        c = s.cell(rr, 1, f"=DCF!$B$22+{dw}")
        c.number_format, c.font, c.fill = PCT, BOLD, HEAD_FILL
        for j in range(len(grows)):
            G = f"{get_column_letter(2 + j)}$4"
            W = f"$A{rr}"
            ev = (f"SUMPRODUCT({fcf},1/(1+{W})^{yrs})"
                  f"+{last_fcf}*(1+{G})/({W}-{G})/(1+{W})^({last_yr}+0.5)")
            c = s.cell(rr, 2 + j, f"=({ev}-{names['debt']}+{names['cash']})/{names['shares']}")
            c.number_format = MONEY
    s.column_dimensions["A"].width = 12
    for col in "BCDEF":
        s.column_dimensions[col].width = 12

    wb.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    vals = dict(SAMPLE)
    if "--inputs" in sys.argv:
        vals.update(json.load(open(sys.argv[sys.argv.index("--inputs") + 1])))
    build(vals, sys.argv[1])
