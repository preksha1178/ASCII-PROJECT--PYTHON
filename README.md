
🎨 ASCII Project (Python)

A fully interactive Python console application that generates large ASCII art for characters, words, numbers, and alphabet ranges using custom-built ASCII patterns.
This project includes Colorama-powered color output, offering Rainbow Mode and Single-Color Mode, making the ASCII text visually appealing.
Designed specifically for Windows terminals, the application is fully menu-driven and uses msvcrt.getch() for fast keypress input.

📑 Table of Contents

About the Project

Features

Color System (Colorama)

How It Works

Project Structure

Installation

Usage

Example Output

Notes

Author

📝 About the Project

This project creates stylized ASCII output by slicing character patterns from predefined ASCII tables.
Users can print one character, full words, alphabet ranges, only alphabets, or only numbers — all with optional color enhancements.

⭐ Features
✔ 1. One Character Mode

Prints a single character in large ASCII art.

✔ 2. Alphanumeric Words Mode

Supports words up to 15 characters including A–Z, digits, and select symbols.

✔ 3. Alphabet Range Mode

Input like:

A-D
M-P
X-Z


Prints ASCII art for all characters in the range.

✔ 4. Only Alphabets Mode

Accepts only A–Z.

✔ 5. Only Numbers Mode

Accepts only digits 0–9.

✔ 6. Color Output System (Powered by Colorama)

Two color modes:

🌈 Rainbow Mode

Each letter appears in a different color (random or rotating sequence).

🎨 Single-Color Mode

Every character block is displayed in the same color.

This makes the ASCII output more expressive and visually vibrant.

🌈 Color System (Using Colorama)

This project uses Colorama, a Python library that enables color text in Windows terminals.

🔹 Why Colorama?

Windows CMD doesn't support ANSI escape codes by default.
Colorama solves this by:

Enabling color output

Auto-resetting colors

Allowing easy use of RGB-like color codes

Ensuring compatibility across Windows terminals

🔹 Installation

Colorama installs automatically with:

pip install colorama

🔹 Usage in Code
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.RED + "Hello")
print(Fore.GREEN + "World")


Your script uses this system to color each letter or whole ASCII block.

🧠 How It Works
🔤 ASCII Pattern Data

The project contains 5 long ASCII strings, each representing one row of the ASCII alphabet, digits, and supported symbols.

Each character occupies exactly 6 columns.

🔁 Printing Mechanism

For every user input:

Calculate the character’s start index

Slice 6-column-wide block

Print it for all 5 rows

Apply Colorama color (Rainbow or Single Color)

Loop until full input is printed

This creates clean, large ASCII text.

📂 Project Structure (ASCII-PROJECT)
ASCII-PROJECT/
│── asciiartproject.py   # Main program
│── README.md            # Documentation

⚙ Installation
1️⃣ Install Python

Download from https://www.python.org/

2️⃣ Clone the Repository
git clone https://github.com/your-username/ASCII-PROJECT.git

3️⃣ Navigate to Folder
cd ASCII-PROJECT

4️⃣ Install Colorama
pip install colorama

5️⃣ Run the Script
python asciiartproject.py

▶ Usage

When you run the script, you will see this menu:

********** ASCII ART PROJECT **********

OPTIONS --

1. One Character
2. Words (Maximum 15 Letters)
3. Range (input in Sequence - Max 15 Letters)
4. Only Alphabets
5. Only Numbers
6. Exit


Choose a mode by pressing the corresponding key (1–6).

🖼 Example Output

Input:

A


Output (example):

 *** 
*   *
*****
*   *
*   *


Colors apply depending on the chosen mode.

⚠ Notes

The project is Windows-specific because it uses:

msvcrt.getch()

os.system("cls")

Maximum input length: 15 characters

Range inputs must be exactly 3 characters (e.g., A-D)

👨‍💻 Author

Preksha Jain
