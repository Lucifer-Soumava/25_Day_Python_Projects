# 21. Folder Analyser

## Overview
`21_Folder_Analyser` is a small Tkinter-based utility that lets you pick a folder and then scans it to produce a quick summary of its contents. It counts the files it finds, calculates the total size, and lists the most common file extensions.

## What it does
- Opens a folder selection dialog instead of asking you to type a path.
- Walks through the selected folder and its subfolders.
- Skips hidden files whose names start with `.`.
- Counts files by extension and reports the top 5 file types.
- Converts total size into megabytes for easier reading.

## Requirements
- Python 3.8+
- `tkinter` for the folder picker dialog

## How to run
From the project folder, run:

```bash
python main.py
```

After the dialog appears, choose a folder to analyse. The script prints the results in the terminal.

## Example output
```text
Folder: C:\Users\Example\Documents
Number of files: 42
Total size (MB): 12.34
Most common file types:
  .txt: 15 files
  .py: 9 files
  .json: 6 files
```

## Notes
- Hidden files are ignored during the scan.
- Files without an extension are counted in the total file count but are not included in the extension breakdown.
- If you cancel the folder picker, the script prints `No folder selected.` and exits.

## Possible improvements
- Add filters so you can include or exclude specific file types.
- Show the largest files in the selected folder.
- Add a simple GUI summary window instead of printing only to the terminal.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)