# 3 — Mad Libs

Overview
- Interactive Mad Libs program that asks the user for parts of speech and injects them into a story template.

Purpose
- Demonstrates string templating, user input prompts, and simple validation.

Thought process / design
- Inputs: nouns, verbs, adjectives, and other placeholders collected via CLI.
- Processing: the program maps each placeholder to the user input and performs safe string formatting.
- Output: the completed story printed to the console. The program may support multiple templates.

Files
- `main.py` — drives the prompt sequence and prints the final story.

How to run
```bash
python main.py
```

Example
- Prompts: "Enter an adjective:" → user `silly`
- Final output: story with `silly` inserted in the right place.

Extensions / Improvements
- Add multiple story templates and let the user choose.
- Add basic input sanitization (e.g., prevent empty input).
- Add unit tests for the templating function.

## 💡 What I learned
- Safely formatting strings and designing simple interactive flows.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)