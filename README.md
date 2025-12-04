🎨 ASCII Art Project (Python)
A fully interactive Windows-based Python console application that generates large, colorful ASCII art for characters, words, numbers, and alphabet ranges.
The project uses predefined ASCII patterns and Colorama-based color output, and provides a smooth menu-driven experience using msvcrt.getch() for instant keypress input.

📑 Table of Contents
About the Project
Features
How It Works
Project Files
Installation
Usage
Example Output
Notes
Author

📝 About the Project
This Python project prints stylized ASCII characters using a predefined 5-line pattern table. Each character is extracted using index slicing and displayed with added color effects, including single-color mode and Rainbow Mode, powered by Colorama.

⭐ Features

✔ 1. One Character Mode
Input one character and view its large ASCII art in color.

✔ 2. Alphanumeric Word Mode
Supports A–Z, 0–9, space and certain symbols (max 15 characters).

✔ 3. Alphabet Range Mode
Enter ranges like:

A-D  
M-P  
X-Z


Displays ASCII art for all letters in the range.

✔ 4. Only Alphabets Mode
Accepts A–Z only; prints colored ASCII characters.

✔ 5. Only Numbers Mode
Accepts digits 0–9 (max 15 characters).

✔ 6. Color Output (Colorama)
• Choose single color output
• Or use Rainbow Mode to print each character in different colors

✔ 7. Menu-Driven Interface
Instant keypress navigation using msvcrt.getch().

🧠 How It Works

🔤 ASCII Pattern Data
The script contains 5 long strings, each representing one row of all characters.
Each character uses 6 columns. Using index math, the correct slice is extracted.

Example logic:

((ord(x) - 64) - 1) * 6     # A–Z  
(ord(x) - 17) * 6           # 0–9


🔁 Printing Mechanism
For each of the 5 ASCII rows:

Calculate the start index

Slice 6 columns

Print them with color

Repeat for each character

This forms clean, large ASCII text.

📂 Project Files
• asciiartproject.py
• README.md

Includes:
• ASCII pattern data
• Color handling with Colorama
• Menu UI
• Input validation
• Character slicing logic
• All five functional modules

⚙ Installation

1️⃣ Install Python
Download from: https://www.python.org/

2️⃣ Clone the Repository

git clone https://github.com/your-username/ASCII-PROJECT.git


3️⃣ Navigate to Folder

cd ASCII-PROJECT


4️⃣ Run the Script

python asciiartproject.py


▶ Usage

You will see:

********** ASCII ART PROJECT **********

OPTIONS --

1. One Character
2. Words (Maximum 15 Letters)
3. Range (input in Sequence - Max 15 Letters)
4. Only Alphabets
5. Only Numbers
6. Exit


Press 1–6 to select any mode.

🖼 Example Output

Input:

A


Output (Example):

 ***  
*   * 
***** 
*   * 
*   * 


(Colors applied based on selected mode.)

⚠ Notes

• Works only on Windows Terminal
• Uses:

msvcrt.getch()

os.system("cls")

colorama.Fore for colors
• Maximum input: 15 characters
• Range input must be like A-D

👨‍💻 Author
PREKSHA Jain
