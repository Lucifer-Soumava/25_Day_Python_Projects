# 8 — Number Guesser Game

Overview
- Terminal-based number guessing game. The program selects a secret number and the player guesses until they find it.

Purpose
- Practice control flow (loops), random number generation, and input validation.

Thought process / design
- Inputs: user guesses via CLI.
- Processing: compare guesses to the secret number, provide high/low hints, count attempts, optionally track best score across sessions.
- Output: success message with the number of attempts; optional best-score persistence.

Files
- `main.py` — game loop, secret generation, and attempt counting.

How to run
```bash
python main.py
```

Example
- Secret number is 42.
- User guesses: `50` → "Too high"
- User guesses: `30` → "Too low"
- User guesses: `42` → "Correct! You guessed it in 3 tries."

Extensions / Improvements
- Add difficulty levels (range size) and persist high scores to a small JSON file.
- Add a `--seed` flag to make the secret number deterministic for testing.

What I learned
- Managing game state and producing friendly user prompts.
