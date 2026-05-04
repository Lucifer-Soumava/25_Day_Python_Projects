# 10 — Currency Converter

Overview
- CLI tool that converts monetary amounts between currencies using local exchange rate data stored in `currencies.json`.

Purpose
- Teach JSON data handling, numeric formatting for currencies, and basic error handling when working with user-supplied codes and amounts.

Thought process / design
- Inputs: amount (numeric), source currency code (e.g., USD), target currency code (e.g., EUR).
- Processing: load `currencies.json` with mapping of currency codes to rates (or rates relative to a base), compute converted amount, and format output with appropriate decimals.
- Validation: verify currency codes exist in `currencies.json` and that the amount parses to a numeric value.
- Output: prints the converted amount and the rate used.

Files
- `main.py` — interactive CLI.
- `currencies.json` — sample rates used by the converter.

How to run
```bash
python main.py
```

Example
- Input: `100 USD to EUR` → Output: `100 USD = 92.50 EUR (rate: 0.925)`

Extensions / Improvements
- Add optional network fetch for live rates (e.g., free exchange rate APIs) with caching and a fallback to local rates.
- Support formatting with currency symbols and locale-aware decimal/group separators using `babel`.

## 💡 What I learned
- Loading JSON, validating user input, and carefully formatting monetary values.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)