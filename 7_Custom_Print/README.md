# 7 — Custom Print

Overview
- Collection of helper utilities to produce nicer console output (alignment, padding, simple colorization, table-like formatting).

Purpose
- Show how to separate presentation logic from business logic and how to make CLI applications more readable.

Thought process / design
- Inputs: arbitrary values or data structures to be displayed.
- Processing: helper functions convert data into aligned strings, padded columns, or simple ASCII tables; optionally add ANSI color codes for emphasis.
- Output: clean, human-friendly console output for small utilities and demos.

Files
- `main.py` — demonstrates helper usage and example outputs.

How to run
```bash
python main.py
```

Example
- Prints a table of sample data with aligned columns and headings.

Extensions / Improvements
- Add a lightweight dependency-free table formatter and tests.
- Provide a `--no-color` flag for environments that don't support ANSI colors.

What I learned
- Practical string operations and designing small reusable utilities for presentation.
