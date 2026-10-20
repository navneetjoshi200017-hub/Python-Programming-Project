# Text Frequency Counter

A command-line Python program that reads a text file, counts how often each word appears, and prints a formatted frequency report. Built as a project for the course **Introduction to Python Programming (CS213)**.

## Features

- Reads any plain-text file from a path you provide
- Cleans words by lowercasing them and stripping surrounding punctuation
- Ignores a built-in list of common stop words (e.g. *the*, *and*, *is*, *they*)
- Lets you add one custom word to ignore
- Shows the top *N* most frequent words, with rank, count and percentage
- Handles errors gracefully (missing file, invalid or non-positive numbers, empty results)

## Project Structure

```
Python-Programming-Project/
├── PythonProject.py   # Entry point: handles user input and program flow
├── word_counter.py    # count_words(): reads the file and counts word frequencies
├── text_utils.py      # clean_word() and get_stop_words() helpers
├── report.py          # get_top_words() and display_report(): formats the output
└── README.md
```

| Module | Responsibility |
| --- | --- |
| `PythonProject.py` | Prompts for the file path, an optional stop word and the number of top words; ties the modules together |
| `word_counter.py` | Reads the file line by line, cleans each word, skips stop words, and returns the word counts and total word count |
| `text_utils.py` | Defines the punctuation set, word cleaning and the default stop-word set |
| `report.py` | Sorts words by frequency and prints the report table |

## Requirements

- Python 3.6 or higher
- No external libraries (standard library only)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/navneetjoshi200017-hub/Python-Programming-Project.git
   cd Python-Programming-Project
   ```

2. Run the program:

   ```bash
   python PythonProject.py
   ```

3. Follow the prompts:
   - **Enter file path:** path to a `.txt` file (e.g. `Test.txt`)
   - **Enter one word to ignore:** optional extra stop word; press Enter to skip
   - **Enter the number of top words to display:** a whole number greater than zero

## Example

```
Enter file path: Test.txt
===Text Frequency Counter===
Enter one word to ignore
(Press Enter to skip):

File read successfully!

Enter the number of top words to display: 5

===================================================
             WORD FREQUENCY REPORT
===================================================

Total words (including stop words) : 120
Words after removing stop words    : 68
Total unique words                 : 41

Top 5 words:
-------------------------------------------------------
Rank  Word                      Frequency  Percentage
-------------------------------------------------------
1     python                           9      13.24%
2     code                             6       8.82%
3     program                          5       7.35%
4     file                             4       5.88%
5     word                             4       5.88%
-------------------------------------------------------
```

*(Numbers above are illustrative; your output depends on your input file.)*

## How It Works

1. The file is read line by line and each line is split into words.
2. Each word is lowercased and stripped of leading/trailing punctuation.
3. Empty results are skipped; every remaining word counts toward the total.
4. Words in the stop-word set are excluded from the frequency dictionary.
5. The dictionary is sorted by frequency (highest first) and the top *N* are displayed, with each word's share of the counted (non-stop) words shown as a percentage.

## Error Handling

- **File not found:** prints a message and exits without crashing
- **Invalid or non-positive limit:** keeps asking until a valid whole number is entered
- **No countable words:** the report shows the totals and a "no words to display" message

## Possible Improvements

- Support multiple custom stop words
- Specify an encoding when opening files (e.g. UTF-8)
- Use `with open(...)` and `collections.Counter` for simpler code
- Export the report to a CSV or text file

## Author

Navneet Joshi, CS213, Introduction to Python Programming
