# 13 — Car Theft Identifier

Overview
- Small rule-based tool that analyzes records about cars and flags entries that match simple suspicious criteria.

Purpose
- Demonstrate rule application, basic heuristics, and how to produce explainable outputs listing why a record was flagged.

Thought process / design
- Inputs: car record fields such as license plate, owner, last seen location, and optional suspicion indicators.
- Processing: apply a set of human-readable rules (e.g., plate not registered, mismatched owner, reported stolen in a dataset) to score or flag records.
- Output: list of flagged records with reasons and severity levels.

Files
- `main.py` — reads sample data or interactive input and runs the rules.

How to run
```bash
python main.py
```

Example
- Input: record with missing owner and an active stolen report → Output: `FLAGGED — missing owner; active stolen report`.

Extensions / Improvements
- Replace heuristics with a more sophisticated classifier (if labeled data is available).
- Add logging and an option to export flagged records to CSV.

## 💡 What I learned
- Encoding domain knowledge as clear rules and presenting explainable results.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)