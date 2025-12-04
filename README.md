🎨 ASCII Art Project (Python)

A fully interactive Python console application that generates large ASCII art for characters, words, alphabets, numbers, and even alphabet ranges.
This project is completely menu-driven, designed specifically for Windows terminals, and uses custom ASCII patterns along with color output (Rainbow Mode & Single-Color Per Letter Mode).

📑 Table of Contents

About the Project

Features

How It Works

Project Structure

Installation

Usage

Example Output

Notes

Author


📝 About the Project

This Python program displays stylized ASCII characters using predefined ASCII patterns stored inside the script. It supports multiple input modes and prints each character in large 6-column block-style ASCII art. The project also includes full color support using ANSI escape sequences.


⭐ Features
✔ 1. One Character Mode

Display a single character in large ASCII form.

✔ 2. Alphanumeric Words Mode

Print words up to 15 characters including A–Z, 0–9, and supported symbols.

✔ 3. Alphabet Range Mode

Input examples:

A-D  
M-P  
X-Z  


The program prints ASCII art for all alphabets within the given range.

✔ 4. Only Alphabets Mode

Accepts only A–Z (max 15 characters).

✔ 5. Only Numbers Mode

Accepts only digits 0–9 (max 15 characters).

✔ 6. Color Output Modes

🌈 Rainbow Mode (each letter gets a unique color)

🎨 Single Color Mode (entire letter printed in one chosen color)

✔ 7. Clean Menu-Driven Interface

Uses msvcrt.getch() for fast key detection and smooth navigation.


🧠 How It Works
🔤 ASCII Pattern Data

The script uses 5 long ASCII strings, each representing a row of the entire alphabet, digits, and symbols.

Each character occupies a fixed 6-column width.

Character slicing logic:

((ord(text) - 64) - 1) * 6      # For A–Z
(ord(x) - 17) * 6               # For 0–9


🔁 Printing Process

For each of the 5 pattern rows:

Calculate character block start index

Slice 6-character segment

Print side-by-side for all letters

Apply color if enabled

This generates the final large ASCII text output.


📂 Project Structure (ASCII-PROJECT)
ASCII-PROJECT/
│── asciiartproject.py   # Main program
│── README.md            # Documentation


⚙ Installation
1️⃣ Install Python

Download from:
https://www.python.org/

2️⃣ Clone the Repository
git clone https://github.com/your-username/ASCII-PROJECT.git

3️⃣ Navigate to Folder
cd ASCII-PROJECT

4️⃣ Run the Script
python asciiartproject.py


▶ Usage

When you run the script, you will see:

********** ASCII ART PROJECT **********

OPTIONS --

1. One Character
2. Words (Maximum 15 Letters)
3. Range (input in Sequence - Max 15 Letters)
4. Only Alphabets
5. Only Numbers
6. Exit


Choose an option by pressing the key (1–6).

🖼 Example Output
Input:
A

Output:
 *** 
*   *
*****
*   *
*   *


(Actual design depends on pattern table.)

⚠ Notes

This project is Windows-only because it uses:

msvcrt.getch()

os.system("cls")

Max input allowed: 15 characters

Range input must be exactly 3 characters (e.g., A-D)

👨‍💻 Author

Preksha Jain
