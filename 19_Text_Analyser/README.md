# 19 - Text Analyser

Overview
- A small command-line utility that reads a text file and prints basic text statistics.

Purpose
- Teach file I/O, regular expressions, collections, and simple text analysis in Python.

Thought process / design
- Inputs: the script currently reads `sample.txt` from the project folder.
- Processing: it lowercases the text, extracts words with a regular expression, counts words, commas, whitespace, punctuation, and calculates the average word length. It also uses `Counter` to find the three most common words.
- Output: a compact summary of the file's content, formatted for quick inspection in the terminal.

Files
- `main.py` — contains the analysis logic and program entry point.
- `sample.txt` — sample text used by the script.

How to run
```bash
python main.py
```

Example output
```text
------------------------------
Word count: 123
Commas used: 4
Character count (incl. whitespaces): 789
Whitespace characters: 130

Top 3 most used words:
> the: 9
> and: 7
> python: 5

Punctuation count: 18
Average word length: 4
------------------------------
```

Notes and limitations
- The script is currently hardcoded to analyse `sample.txt`, so renaming or moving that file will break the run until the path is updated.
- If the file contains no words, the average word length calculation will fail; that is a useful follow-up improvement.

Extensions / Improvements
- Allow the filename to be passed as a command-line argument.
- Add handling for empty files or files with no word matches.
- Report additional statistics such as line count, sentence count, and unique word count.

## 💡 What I learned
- Working with regex-based tokenisation, `Counter`, and simple terminal reporting for text analysis.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)