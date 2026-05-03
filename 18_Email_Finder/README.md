# 18 — Email Finder

Overview
- A small utility that scans text files for email-like patterns using regular expressions and prints deduplicated matches with optional surrounding context.

Purpose
- Teach text processing with regex, file I/O, and simple result filtering/deduplication.

Thought process / design
- Inputs: one or more file paths supplied interactively or via command-line; can also accept pasted text.
- Processing: read file contents, apply a conservative regular expression to capture common email address patterns, normalize and deduplicate results, and optionally show the line number and surrounding lines for context.
- Output: a clean list of found email addresses and the source file/line where they were found.

Files
- `main.py` — contains scanning logic and CLI handling.
- `file.txt`, `website_example.txt` — sample text files used for testing.

How to run
```bash
python main.py file.txt
python main.py website_example.txt
```

Example output
```
Found 3 email(s):
- alice@example.com (file.txt:12)
- contact@website.example (website_example.txt:4)
- bob.surname@domain.co.uk (file.txt:8)
```

Notes, limitations & ethics
- The regex is intentionally simple and may produce false positives or miss some valid addresses; it's meant for learning and basic scanning only.
- Do not use this tool for scraping or harvesting addresses without permission. Respect privacy and applicable laws.

Extensions / Improvements
- Add CLI flags for recursive directory scanning, output formats (CSV/JSON), and context window size.
- Add unit tests for the regex and deduplication logic.

What I learned
- Practical regex usage, file reading patterns, and safe handling of text processing outputs.
