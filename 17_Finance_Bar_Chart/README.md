# 📊 Personal Finance Dashboard

A dynamic personal finance visualizer built with Python. Charts automatically update when the CSV data file is changed — no code editing needed.

---

## 🖼️ Output

The program generates two bar charts side by side:
- **Monthly Overview** — Income, Rent, Food, Taxes, and Other Expenses
- **Yearly Overview** — Total Income, Total Expenses, and Savings

---

## 📁 Project Structure

```
finance-dashboard/
├── finance_dashboard.py   # Main Python script
├── Book1.csv              # Input data file (edit this to update charts)
└── README.md
```

---

## 📄 CSV Format

The program reads from `Book1.csv`. Your file should have these columns:

| Monthly Income | Rent | Food | Tax_Rates | Other_Expenses |
|----------------|------|------|-----------|----------------|
| 5000 | 1200 | 400 | 0.2 | 300 |

> **Tip:** Just change the values in the CSV and run the script again — the charts will update automatically.

---

## ▶️ How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/finance-dashboard.git
   cd finance-dashboard
   ```

2. Install the required library
   ```bash
   pip install matplotlib
   ```

3. Run the script
   ```bash
   python finance_dashboard.py
   ```

---

## 🛠️ Built With

- Python 3
- Matplotlib — for bar chart visualization
- CSV module — for reading dynamic data from file

---

## 💡 What I Learned

- Reading and parsing CSV files using Python's `csv.DictReader`
- Creating multi-panel visualizations using `matplotlib.subplots`
- Calculating derived financial metrics (taxes, yearly savings) from raw data
- Making data-driven charts that update dynamically without changing code

---

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)