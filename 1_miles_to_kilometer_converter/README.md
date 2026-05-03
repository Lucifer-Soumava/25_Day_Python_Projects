# 1 — Miles to Kilometer Converter

Overview
- Small command-line utility that converts distances from miles to kilometers.

Purpose
- Provide a beginner-friendly example of reading user input, validating it, performing arithmetic operations, and printing formatted output.

Thought process / design
- Inputs: a numeric value representing miles (supports integers and floats).
- Processing: multiplies the input by the conversion factor 1.60934 to compute kilometers.
- Validation: attempts to parse user input to `float`; rejects non-numeric values with a helpful message and a retry loop.
- Output: prints the resulting kilometers with controlled decimal precision.

Files
- `main.py` — entry point. Reads input, validates, converts, prints result.

How to run
1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

Example
1. Program asks: "Enter miles:"
2. User types `5` → Program prints `5 miles = 8.05 kilometers` (example formatting)

Extensions / Improvements
- Add unit tests for the converter function.
- Support batch conversions from a file (CSV input).
- Add a small GUI or web front-end for demonstration.

What I learned
- Basic CLI input/output in Python, input validation, and formatting numeric output.
