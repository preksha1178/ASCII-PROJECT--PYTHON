# 🎨 ASCII Art Project (Python)

A fully interactive Windows-based Python console application that generates large, colorful ASCII art for characters, words, numbers, and alphabet ranges. The project uses predefined ASCII patterns and Colorama-based color output, and provides a smooth menu-driven experience using `msvcrt.getch()` for instant keypress input.

## 📑 Table of Contents
- About the Project
- Features
- How It Works
- Project Files
- Installation
- Usage
- Example Output
- Notes
- Author

## 📝 About the Project
This Python project prints stylized ASCII characters using a predefined 5-line pattern table. Each character is extracted using index slicing and displayed with added color effects, including single-color mode and Rainbow Mode, powered by Colorama.

## ⭐ Features
- ✔ **One Character Mode** – Input one character and view its large ASCII art in color.
- ✔ **Alphanumeric Word Mode** – Supports A–Z, 0–9, space and certain symbols (max 15 characters).
- ✔ **Alphabet Range Mode** – Enter ranges like `A-D`, `M-P`, `X-Z` to display ASCII art for all letters in the range.
- ✔ **Only Alphabets Mode** – Accepts A–Z only; prints colored ASCII characters.
- ✔ **Only Numbers Mode** – Accepts digits 0–9 (max 15 characters).
- ✔ **Color Output (Colorama)** – Choose single color output or Rainbow Mode to print each character in different colors.
- ✔ **Menu-Driven Interface** – Instant keypress navigation using `msvcrt.getch()`.

## 🧠 How It Works

### 🔤 ASCII Pattern Data
- The script contains 5 long strings, each representing one row of all characters.
- Each character uses 6 columns; index math extracts the correct slice.

Example index formulas:

A–Z
start = ((ord(x) - 64) - 1) * 6

0–9
start = (ord(x) - 17) * 6


### 🔁 Printing Mechanism
- For each of the 5 ASCII rows, the program calculates the start index, slices 6 columns, and prints them with color.
- This repeats for every character in the input to form clean, large ASCII text.

## 📂 Project Files
- `asciiartproject.py`
- `README.md`

The project includes:
- ASCII pattern data  
- Color handling with Colorama  
- Menu-based UI  
- Input validation  
- Character slicing logic  
- All five functional modules

## how to install Colorama:
pip install colorama

## ⚙ Installation

1️⃣ Install Python (if not installed)
Download from: https://www.python.org/

2️⃣ Clone the repository
git clone https://github.com/your-username/ASCII-PROJECT.git

3️⃣ Navigate to the project folder
cd ASCII-PROJECT

4️⃣ Run the script
python asciiartproject.py



## ▶ Usage

When you run the script, you will see:

** ASCII ART PROJECT **

## OPTIONS --

One Character

Words (Maximum 15 Letters)

Range (input in Sequence - Max 15 Letters)

Only Alphabets

Only Numbers

Exit

Press 1–6 to select any mode.


Choose the desired option, enter your input (character, word, range, etc.), and the corresponding ASCII art will be printed in color.

## 🖼 Example Output

Input:

A

Output (example):

 ***  
*   * 
***** 
*   * 
*   * 



(Colors are applied based on the selected mode.)

## ⚠ Notes
- Works only on Windows Terminal.
- Uses:
  - `msvcrt.getch()` for instant keypress input
  - `os.system("cls")` to clear the screen
  - `colorama.Fore` for color output
- Maximum input: 15 characters.
- Range input must be in the form `A-D`, `M-P`, etc.

## 👨‍💻 Author
Preksha Jain

