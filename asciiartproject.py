import os
import msvcrt as msv
import sys
from colorama import Fore, Back, Style, init
init(autoreset=True)

# ------------------ COLOR SELECTION ------------------
def chooseColor():
    os.system("cls")
    print("\n\n***** SELECT TEXT COLOR *****\n")
    print("1. RED")
    print("2. GREEN")
    print("3. YELLOW")
    print("4. BLUE")
    print("5. MAGENTA")
    print("6. CYAN")

    choice = input("\nEnter Color Number (1-6): ").strip()

    if choice == "1": return Fore.RED
    if choice == "2": return Fore.GREEN
    if choice == "3": return Fore.YELLOW
    if choice == "4": return Fore.BLUE
    if choice == "5": return Fore.MAGENTA
    if choice == "6": return Fore.CYAN

    print("\nInvalid color! Try again.")
    msv.getch()
    return chooseColor()

# ------------------------------------------------------

data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

# -------------------------------------------------------------

def oneCharacter():
    os.system("cls")
    color = chooseColor()

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"One Character Module","*"*10,end="\n\n")

    text = input("Enter a Character (Only One Character) -- ").upper()
    
    if len(text) != 1:
        print("\n\nPlease Enter Only One Letter -- \n\n")
        oneCharacter()
        return

    n = (ord(text)-17)*6 if text.isdigit() else ((ord(text)-64)-1)*6

    for row in data:
        for col in range(n, n+6):
            print(color + row[col], end="")
        print()

# -------------------------------------------------------------

def alphaNumWords():
    os.system("cls")
    color = chooseColor()
    sys.stdin.flush()

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Numeric Words Module","*"*10,end="\n\n")

    text = input("Enter String (Only <= 15 Character) -- ").upper()
    
    if not (1 <= len(text) <= 15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        alphaNumWords()
        return

    for row in data:
        for ch in text:
            n = (ord(ch)-17)*6 if ch.isdigit() else ((ord(ch)-64)-1)*6
            for col in range(n, n+6):
                print(color + row[col], end="")
        print()

# -------------------------------------------------------------

def alphaRange():
    os.system("cls")
    color = chooseColor()
    sys.stdin.flush()

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Range Module","*"*10,end="\n\n")

    text = input("Enter Range in Format (A-D) -- ").upper()

    if len(text) != 3:
        print("\n\nPlease Enter Valid Range -- \n\n")
        alphaRange()
        return

    sr = ord(text[0]) - 64
    er = ord(text[2]) - 64

    if sr > er:
        print("\n\nRange must be in sequence -- \n\n")
        alphaRange()
        return

    for row in data:
        for x in range(sr, er+1):
            start = (x-1) * 6
            for col in range(start, start+6):
                print(color + row[col], end="")
        print()

# -------------------------------------------------------------

def onlyAlpha():
    os.system("cls")
    color = chooseColor()
    sys.stdin.flush()

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Alphabets Module","*"*10,end="\n\n")

    text = input("Enter Alphabets Only (<= 15) -- ").upper()

    if not text.isalpha():
        print("\n\nPlease Enter Only Alphabets -- \n\n")
        onlyAlpha()
        return

    for row in data:
        for ch in text:
            n = ((ord(ch) - 64) - 1) * 6
            for col in range(n, n+6):
                print(color + row[col], end="")
        print()

# -------------------------------------------------------------

def onlyNum():
    os.system("cls")
    color = chooseColor()
    sys.stdin.flush()

    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Numbers Module","*"*10,end="\n\n")

    text = input("Enter Numbers Only (<= 15) -- ")

    if not text.isdigit():
        print("\n\nPlease Enter Only Digits -- \n\n")
        onlyNum()
        return

    for row in data:
        for ch in text:
            n = (ord(ch)-17)*6
            for col in range(n, n+6):
                print(color + row[col], end="")
        print()

# -------------------------------------------------------------

def mainUI():
    os.system("cls")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("OPTIONS -- \n\n")
    print("1. One Character")
    print("2. Words (Maximum 15 Letters)")
    print("3. Range (A-D)")
    print("4. Only Alphabets")
    print("5. Only Numbers")
    print("6. Exit")
    print("\n\nEnter Your Choice -- ",end="")

    ch = msv.getch().decode()

    if ch == "1": oneCharacter()
    elif ch == "2": alphaNumWords()
    elif ch == "3": alphaRange()
    elif ch == "4": onlyAlpha()
    elif ch == "5": onlyNum()
    elif ch == "6": return

    print("\n\nDo you want to continue Project? Press Y else any key...")
    if msv.getch().decode().lower() == "y":
        mainUI()

mainUI()
