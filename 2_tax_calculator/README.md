# 2 — Tax Calculator

Overview
- Simple income tax calculator demonstrating conditional logic, bracket calculations, and formatted output.

Purpose
- Teach applying tax brackets/rates to compute tax liabilities, and how to present a breakdown of deductions and net income.

Thought process / design
- Inputs: gross income (numeric) and optional parameters (filing status, deductions).
- Processing: either apply a single flat rate or iterate through predefined brackets to compute tax by bracket.
- Output: detailed breakdown showing gross income, tax per bracket (if applicable), total tax, and net income.

Files
- `main.py` — includes the calculator and a small interactive prompt.

How to run
```bash
python main.py
```

Example run
- Enter gross income: `50000`
- Program output:
	- Gross income: 50000
	- Tax (brackets): 8000
	- Net income: 42000

Extensions / Improvements
- Add configuration for different countries/tax years.
- Add CLI flags to run calculations non-interactively and output JSON for automation.
- Add unit tests covering edge cases and bracket boundaries.

What I learned
- Implementing bracketed calculations and presenting clear user-friendly summaries.
