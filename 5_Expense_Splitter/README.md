# 5 — Expense Splitter

Overview
- Utility to split expenses among participants with optional adjustments (discounts, paid-by-one-person, etc.).

Purpose
- Demonstrates arithmetic operations, rounding strategies, and handling special cases (e.g., unequal shares).

Thought process / design
- Inputs: total bill amount, number of participants, optional per-person adjustments (items paid separately), and rounding preferences.
- Processing: compute base share, apply adjustments for special cases, ensure totals sum to original amount (handle rounding residuals).
- Output: per-person amount due and a brief summary table.

Files
- `main.py` — interactive prompt and core calculation logic.

How to run
```bash
python main.py
```

Example
- Total: `120.00`, People: `3` → prints `Each person owes 40.00`.

Extensions / Improvements
- Support items list CSV input where each item has a payer and cost.
- Add tip percentage and tax calculation options.
- Provide a `--rounding` flag to choose rounding behavior.

## 💡 What I learned
- Handling floating point rounding issues and designing UIs for small utilities.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)