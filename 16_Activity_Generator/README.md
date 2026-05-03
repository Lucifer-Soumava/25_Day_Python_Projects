# 16 — Activity Generator

Overview
- Utility that suggests random activities from a local dataset (`activities.json`). Supports simple filtering and multiple output formats.

Purpose
- Demonstrate reading JSON data, filtering, random selection, and presenting results in a user-friendly format.

Thought process / design
- Inputs: optional filters like activity type, number of participants, or difficulty.
- Processing: load `activities.json`, apply filters, randomly choose a matching activity, and format output.
- Output: human-friendly suggestion with details (title, description, participants, estimated time).

Files
- `main.py` — interactive selector and formatting helpers.
- `activities.json` — sample activities dataset.

How to run
```bash
python main.py
```

Example
- `Find me an activity for 2 people` → "Try: Board games (45–90 mins) — Cooperative or competitive depending on the game."

Extensions / Improvements
- Add command-line flags for non-interactive usage and output as JSON for automation.
- Allow user-submitted activities to be appended to the local dataset.

What I learned
- Working with JSON and the `random` module; designing small filter pipelines.
