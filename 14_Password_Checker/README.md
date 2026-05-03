# 14 — Password Checker

Overview
- Command-line password strength checker that evaluates passwords against several heuristics and a local blacklist (`common_passwords.txt`).

Purpose
- Teach security-minded checks: length, character class diversity, and blacklist membership; provide actionable suggestions to improve weak passwords.

Thought process / design
- Inputs: password string entered by the user (stdin).
- Processing: evaluate length, presence of lowercase/uppercase/digits/symbols, and membership in `common_passwords.txt`. Compute a numeric or categorical strength assessment and produce targeted recommendations.
- Output: readable assessment (e.g., "Weak", "Moderate", "Strong") with suggestions like "Add symbols" or "Increase length to 12+ characters".

Files
- `main.py` — interactive checker.
- `common_passwords.txt` — local blacklist used to catch commonly used passwords.

How to run
```bash
python main.py
```

Example
- Input: `password123` → Output: "Weak — uses common patterns; add symbols and increase length."

Extensions / Improvements
- Add zxcvbn or another statistical strength estimator for richer scoring.
- Offer a password generator that produces strong suggestions.
- Add unit tests for each rule and blacklist checks.

What I learned
- Practical security checks and how to present actionable feedback to users.
