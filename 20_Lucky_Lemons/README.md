# 20 - Lucky Lemons

Overview
- A small terminal slot machine game where you bet credits and spin three fruit symbols.

Purpose
- Practice loops, classes, randomness, simple game-state management, and input validation in Python.

Thought process / design
- Inputs: user enters a bet amount each round.
- Processing:
  - The game starts with `200` credits.
  - A valid bet is deducted from credits before the spin.
  - Three symbols are picked at random from: `🍒`, `🍇`, `🍊`, `🍋`.
  - Full match payout: all three symbols match, payout is `(symbol value sum) * bet`.
  - Partial payout: first two symbols match, payout is half the two-symbol value total times bet.
- Output: prints the spin result, credits won, and remaining credits after each round.

Symbol values
- `🍒` = `1`
- `🍇` = `2`
- `🍊` = `3`
- `🍋` = `5`

Files
- `main.py` - contains the `SlotMachine` class and program entry point.

How to run
```bash
python main.py
```

Example play
```text
Starting credits: 200
------------------------------
Bet: 10
🍋🍋🍊
Credits won 50
Credits remaining: 240
------------------------------
Bet: 20
🍇🍇🍇
Credits won: 120
Credits remaining: 340
------------------------------
```

Notes and limitations
- Entering non-numeric input is handled and prompts again.
- If credits reach `0`, the program exits with `Game Over!`.
- The game currently runs until credits are exhausted or the user manually stops it.

Extensions / Improvements
- Add a quit command (for example `q`) during betting.
- Add a minimum/maximum bet rule.
- Track and display spin history and best win.
- Add configurable starting credits and symbol sets.

## 💡 What I learned
- Building a small game loop with object-oriented design, random events, and payout rules.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)
