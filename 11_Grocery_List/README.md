# 11 — Grocery List

Overview
- Interactive grocery list manager to add, remove, and view shopping items; demonstrates simple CRUD-style CLI interactions.

Purpose
- Practice list/dictionary manipulation, persistence (optional), and designing a simple command-driven interface.

Thought process / design
- Inputs: item name, optional quantity, commands (add/remove/list/clear/quit).
- Processing: maintain an in-memory list or dictionary of items and quantities; optional persistence to a file (e.g., JSON) for state between runs.
- Output: nicely formatted shopping list and quick summaries (total items).

Files
- `main.py` — interactive loop and basic persistence hooks (if implemented).

How to run
```bash
python main.py
```

Example session
- `add milk 2` → Now `milk: 2`
- `list` → prints items and quantities

Extensions / Improvements
- Persist list to `grocery.json` between runs.
- Add import/export from CSV and a `--sort` flag for alphabetical lists.

What I learned
- Building a small stateful command loop and organizing operations for testability.
