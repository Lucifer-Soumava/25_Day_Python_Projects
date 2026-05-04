# 9 — Website Stats

Overview
- Small utility to analyze basic website statistics from local sample data (logs or CSV). Designed as a parsing and aggregation exercise.

Purpose
- Demonstrate text parsing, aggregation, and presenting concise summaries of web logs or metrics.

Thought process / design
- Inputs: a local sample log file or CSV with events/hits.
- Processing: parse lines, extract fields (timestamp, URL/path, status, bytes), aggregate by metric (counts per page, total hits, error counts).
- Output: summary report listing top endpoints, total hits, and a few simple derived metrics.

Files
- `main.py` — parsing and reporting logic.

How to run
```bash
python main.py
```

Example output
- Total hits: 512
- Top endpoints:
	1. /index.html — 120 hits
	2. /about — 45 hits

Extensions / Improvements
- Add CLI flags to filter by date range or to output JSON.
- Add support for standard log formats (combined/common) and unit tests for parsing.

## 💡 What I learned
- Robust text parsing, defensive programming for malformed lines, and summarizing large datasets in concise reports.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)