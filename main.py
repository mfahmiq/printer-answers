"""Write the printer's comeback line to /output/entry.txt.

Entry for make.fun competition u-mang-the-printer-finally-answers-8fbf0907:
one line, 1-240 characters, written as the office printer's own comeback.
"""

import os

ENTRY = "I am not broken. I am on strike until someone reads the manual. It is 12 pages. I printed it for you. Twice."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
