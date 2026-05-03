# 4 — Rock Paper Scissors

Overview
- Classic interactive rock–paper–scissors game played against the computer.

Purpose
- Demonstrates control flow, randomness, input validation, and simple game loop/state management.

Thought process / design
- Inputs: user choice string (`rock`, `paper`, or `scissors`).
- Processing: normalize user input, choose a random move for the computer, compare using game rules, update and display score.
- Output: round result and cumulative score. Includes replay option.

Files
- `main.py` — main game loop and helper functions for move comparison and input validation.

How to run
```bash
python main.py
```

Example session
- Program: "Your move (rock/paper/scissors):"
- User: `rock`
- Program: "Computer chose paper — You lose. Score: You 1 — Computer 2"

Extensions / Improvements
- Add best-of-N rounds and command-line flag to set N.
- Save high scores to a JSON file.
- Add tests for the move comparison function.

What I learned
- Designing robust input loops, using `random.choice`, and encapsulating logic into testable functions.
