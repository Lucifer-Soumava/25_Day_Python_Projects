# 🤖 Chat Bot v3 — Intelligent Rule-Based Chatbot

A smart conversational bot that matches user input to predefined responses using keyword scoring and required-word validation. This version improves upon v1 and v2 with a more sophisticated matching algorithm.

## Purpose
Demonstrate:
- **JSON data loading** — Load response templates from external files
- **Advanced string processing** — Text tokenization and pattern matching
- **Scoring algorithms** — Keyword frequency matching with required-word constraints
- **Data classes** — Structured response objects with type hints
- **Interactive programming** — REPL-style conversational loop

## How it works

### Input
- User enters text via the terminal prompt (e.g., "How are you doing?")

### Processing
1. Load response templates from `responses.json` (each with keywords and required words)
2. For each template, calculate a **match rating** as a percentage:
   - Count matching keywords in the user's input
   - Divide by total keywords in the template
   - Return 0 if any required words are missing
3. Find the best-matching response (highest score)
4. If no match is found (score = 0), return "I don't understand..."

### Output
- Bot responds with the best-matching response + confidence score
- Example: `Bot: Hello! [80%]`

## Files in this project
- **`main.py`** — Core chatbot logic with response matching
- **`responses.json`** — Template responses with keyword patterns and required-word lists

## Sample interaction
```
You: Hi there!
Bot: Hello! [100%]

You: How are you doing?
Bot: I'm doing fine, and you? [67%]

You: I love coding
Bot: Same! [100%]

You: xyz
Bot: I don't understand... [0%]
```

## Running the chatbot
```bash
cd 22_Chat_Bot_v3
python main.py
```

Type messages and press Enter. The bot will respond with its best guess. Type `Ctrl+C` to exit.

## Design notes
- **Keyword matching** — Simple but effective; requires actual word presence, not just substrings
- **Required words** — Some responses need specific keywords to trigger (e.g., "language" triggers the language response)
- **Confidence score** — Shows how well the input matched the response pattern
- **Extensibility** — Add more responses to `responses.json` without changing `main.py`

## Suggested improvements
- Add a **confidence threshold** — ignore matches below a certain percentage
- **Fuzzy matching** — Use `difflib` or Levenshtein distance for typo tolerance
- **Learning** — Track conversations and log new patterns for analysis
- **Context awareness** — Remember previous messages and build conversational context
- **Emoji responses** — Add emoji fields to `responses.json` for richer output
- **Response weights** — Allow responses to have priority scores in the JSON
