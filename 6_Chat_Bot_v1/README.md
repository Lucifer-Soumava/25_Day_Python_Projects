# 6 — Chat Bot v1

Overview
- Minimal rule-based chat bot running in the terminal. Responds to keyword triggers with canned replies.

Purpose
- Introduce chatbot basics: parsing user text, mapping intents via simple rules, and replying synchronously.

Thought process / design
- Inputs: user text messages typed into the terminal.
- Processing: normalize input (lowercase, strip punctuation), run against a prioritized list of keyword patterns or phrases, and return the first matching canned response.
- Output: prints the bot's reply and prompts for the next user message.

Files
- `main.py` — contains the message loop and matching logic; responses stored in a dictionary or list.

How to run
```bash
python main.py
```

Example
- User: "Hello"
- Bot: "Hi! How can I help you today?"

Extensions / Improvements
- Add state tracking (remember user name or previous topic).
- Replace rule-based matching with a tiny NLP library or embed simple pattern scoring.
- Add unit tests for the message processing functions.

## 💡 What I learned
- Building simple conversational flows and organizing response rules for testability.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)