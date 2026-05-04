# 15 — Chat Bot v2

Overview
- An improved terminal chat bot that expands on the rule-based approach by adding simple state tracking and more flexible response rules.

Purpose
- Demonstrate design techniques for conversational agents without heavy dependencies: intent matching, statefulness, and modular response handlers.

Thought process / design
- Inputs: user messages via terminal.
- Processing: normalize text, detect intent using a prioritized list of patterns (or simple regex), maintain a minimal session state (e.g., user name, last topic), and choose a response generator that may reference state.
- Output: the bot's reply and follow-up prompts. Responses are designed to be short, helpful, and deterministic for testability.

Files
- `main.py` — core loop and state management.

How to run
```bash
python main.py
```

Example conversation
- User: "My name is Alex"
- Bot: "Nice to meet you, Alex! What can I help with today?"

Extensions / Improvements
- Add an external configuration file for response templates to make the bot data-driven.
- Add unit tests for intent detection and response generation.

## 💡 What I learned
- Organizing conversational code, keeping state minimal, and writing rule-based intent handlers.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)