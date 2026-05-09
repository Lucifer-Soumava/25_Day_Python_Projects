# Website Analyser

## Overview
`23_Website_Analyser` is a small async command-line utility that checks whether a list of websites is online and how long each request takes to complete.

## What it does
- Accepts a list of website URLs in `main.py`.
- Adds `https://` automatically when a URL does not include a scheme.
- Sends each request in a background thread using `asyncio.to_thread`.
- Prints whether each site is online, along with the HTTP status code, reason phrase, and response time.
- Reports timeouts and other request errors without stopping the whole run.

## Requirements
- Python 3.8+
- `requests`

## How to run
From the project folder, run:

```bash
python main.py
```

The script checks the websites defined in the `urls` list and prints the results to the terminal.

## Example output
```text
Checking 12 websites...
https://www.apple.com: ✅ ONLINE (200 OK [0.42s])
Could not retrieve information for: "https://nonexistent-website-404.com"
Timeout reached — some websites took too long.
Done!
```

## Notes
- Website availability can vary by network, region, and temporary outages.
- The script currently uses a fixed timeout value and checks a hard-coded list of websites.
- If a URL already includes `http://` or `https://`, it is left unchanged.

## Possible improvements
- Let the user enter URLs at runtime instead of editing the list in code.
- Read URLs from a text file or CSV.
- Add command-line arguments for timeout and verbosity.
- Show a summary table with success and failure counts.

## 👤 Author

**Soumava Pramanick**  
2nd Year B.Tech Student  
[GitHub](https://github.com/Lucifer-Soumava)