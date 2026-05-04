# 🎯 25 Day Python Projects
# 🎯 25 Day Python Projects

Welcome — this repo is a curated collection of small, focused Python projects created for learning, classroom exercises, and quick demos. Each project is intentionally compact so you can read, run, and modify it in a few minutes.

Why this repo exists
- 📚 Teach and practice core Python skills with bite-sized projects: file I/O, regular expressions, JSON/CSV handling, classes and OOP, data visualization, and simple interactive programs (games and utilities).
- ⚡ Provide ready-to-run examples with minimal dependencies so learners can experiment immediately.

How the repository is organized
- 🗂️ Folders are prefixed with a number (1..19) to indicate sequence and are named for quick recognition. (More to be added later.)
- ▶️ Each project contains a `main.py` entry point plus any sample data files required to run the example (CSV, JSON, TXT, etc.).
- 📄 Each project folder includes a `README.md` that explains the project's purpose, input/output expectations, design/thought-process, run instructions, and suggested improvements.

Get started — quick run
1. Open a terminal in this workspace root.
2. Change into any project folder, for example:

```bash
cd "1_miles_to_kilometer_converter"
python main.py
```

Project summaries (what each folder is about)
- 🛣️ `1_miles_to_kilometer_converter` — Convert miles ↔ kilometers. Shows simple I/O and arithmetic with input validation.
- 💸 `2_tax_calculator` — Calculate tax by brackets or flat rates and show breakdowns.
- ✍️ `3_Mad_Libs` — Interactive story templating by asking for parts of speech.
- ✊📄 `4_Rock_Paper_Scissors` — Simple terminal game vs computer using `random`.
- 🧾 `5_Expense_Splitter` — Split bills among participants and handle rounding/adjustments.
- 🤖 `6_Chat_Bot_v1` — Rule-based chatbot with keyword matching and canned responses.
- 🎨 `7_Custom_Print` — Helper utilities for prettier console output (alignment, simple tables, colors).
- 🔢 `8_Number_Gusser_Game` — Number-guessing game demonstrating loops and state.
- 📈 `9_Website_Stats` — Parse sample logs/CSV to produce basic site metrics and top endpoints.
- 💱 `10_Currency_Converter` — Convert currencies using local `currencies.json`; demonstrates JSON parsing and numeric formatting.
- 🛒 `11_Grocery_List` — CLI CRUD for a shopping list with optional persistence.
- 🚗 `12_Car_Factory` — Small OOP example: constructing `Car` objects and simulating a production pipeline.
- 🚨 `13_Car_Theft_Identifier` — Rule-based heuristics to flag suspicious car records (educational only).
- 🔐 `14_Password_Checker` — Password-strength heuristics and blacklist checks using `common_passwords.txt`.
- 🗣️ `15_Chat_Bot_v2` — Enhanced chat bot with minimal state and improved response handling.
- 🎲 `16_Activity_Generator` — Random activity suggestions from `activities.json` with optional filters.
- 📊 `17_Finance_Bar_Chart` — Detailed finance dashboard that reads `Book1.csv` and produces bar charts (use this README as reference for detail and style).
- ✉️ `18_Email_Finder` — Scan text files for email-like patterns using regex; outputs deduplicated findings and context.
- 📝 `19_Text_Analyser` — Read a sample text file and report counts, punctuation, and the most common words.

Design & thought process (applies to most projects)
- 🔍 Inputs: Each project documents typical inputs (CLI prompts, sample files, or arguments).
- ⚙️ Processing: Projects focus on one or two tasks — parsing, computing, formatting, or interacting — and keep logic small and testable.
- 🖨️ Outputs: Clear terminal output, sample files, or small visualizations (e.g., the finance project uses matplotlib).

Tips for running and testing
- 🐍 Use Python 3.8+ for best compatibility.
- 📦 If a project depends on an external library (e.g., `matplotlib` for charts), the project's README will call it out and suggest installing via:

```bash
pip install matplotlib
```

- ⚙️ To run a project non-interactively, consider adding simple CLI flags to `main.py` (many projects currently use interactive prompts).

Contributing
- 🤝 Improve a project's README with examples or edge-case explanations.
- ✅ Add unit tests for parsing/logic-heavy projects and include instructions in the project's README.
- 📬 Create a PR with a descriptive title and explain the change in the body.

Ethics & usage
- ⚖️ Some tools (e.g., `18_Email_Finder`) scan content; do not use them to harvest or scrape personal data without consent. Respect privacy and local laws.

Next recommended improvements
- 🚀 Add `requirements.txt` or `pyproject.toml` where external packages are used.
- 🧪 Add basic unit tests and a top-level `run_all_examples.sh` (or Windows equivalent) to quickly validate each project.

License & credits
- 👤 Author: Lucifer-Soumava
- 📜 These are educational/course projects. Add a license file (for example MIT) if you plan to publish or share broadly.


## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)