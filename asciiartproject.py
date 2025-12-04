import os
import msvcrt as msv
import sys
import random
from colorama import Fore, init
init(autoreset=True)

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

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
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"One Character Module","*"*10,end="\n\n")
    text = input("Enter a Character (Only One Character) -- ").upper()
    if len(text) != 1:
        print("\n\nPlease Enter Only One Letter -- \n\n")
        oneCharacter()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else \
            26*6 if text ==" " else 27*6 if text=="@" else 28*6 if text=="_" else \
            29*6 if text=="-" else 30*6 if text=="." else ((ord(text)-64)-1)*6

        col = random.choice(colors)  # One color for whole letter

        for i in data:
            for j in range(n, n+6):
                print(col + i[j], end="")
            print()

# -------------------------------------------------------------

def alphaNumWords():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Numeric Words Module","*"*10,end="\n\n")
    text = input("Enter String (Only <= 15 Character) -- ").upper()
    if not (1 <= len(text) <= 15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        alphaNumWords()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))

        for i in data:
            for x in text:
                col = random.choice(colors)  # NEW: one color for each letter

                n = (ord(x)-17)*6 if ord(x)>=48 and ord(x)<=57 else \
                    26*6 if x==" " else 27*6 if x=="@" else 28*6 if x=="_" else \
                    29*6 if x=="-" else 30*6 if x=="." else ((ord(x)-64)-1)*6

                for j in range(n, n+6):
                    print(col + i[j], end="")
            print()

# -------------------------------------------------------------

def alphaRange():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Range Module","*"*10,end="\n\n")
    text = input("Enter Range Between (1 to 15 Character) & in Sequence Like (A-D) -- ").upper()

    if len(text) != 3:
        print("\n\nPlease Enter Valid Range -- \n\n")
        alphaRange()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        sr = (ord(text[0]) - 64)
        er = (ord(text[2]) - 64)

        if sr > er or (er - sr >= 15):
            print("\n\nPlease Enter Valid Range in Sequence -- \n\n")
            msv.getch()
            alphaRange()
        else:
            for i in data:
                for x in range(sr, er+1):
                    col = random.choice(colors)  # NEW

                    n = (x - 1) * 6
                    for j in range(n, n+6):
                        print(col + i[j], end="")
                print()

# -------------------------------------------------------------

def onlyAlpha():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Alphabets Module","*"*10,end="\n\n")
    text = input("Enter String (Only <= 15 Character) -- ").upper()

    if not (1 <= len(text) <= 15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        msv.getch()
        onlyAlpha()
    else:
        if not text.isalpha():
            print("\n\nPlease Enter Only Alphabets -- \n\n")
            msv.getch()
            onlyAlpha()
        else:
            print("\n\nYou Entered -- {0}\n\n".format(text))

            for i in data:
                for x in text:
                    col = random.choice(colors)

                    n = ((ord(x) - 64) - 1) * 6
                    for j in range(n, n+6):
                        print(col + i[j], end="")
                print()

# -------------------------------------------------------------

def onlyNum():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Only Numbers Module","*"*10,end="\n\n")
    text = input("Enter String (Only <= 15 Character) -- ").upper()

    if not (1 <= len(text) <= 15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        msv.getch()
        onlyNum()
    else:
        if not text.isnumeric():
            print("\n\nPlease Enter Only Numbers -- \n\n")
            msv.getch()
            onlyNum()
        else:
            print("\n\nYou Entered -- {0}\n\n".format(text))

            for i in data:
                for x in text:
                    col = random.choice(colors)

                    n = (ord(x)-17)*6 if x.isdigit() else ((ord(x)-64)-1)*6
                    for j in range(n, n+6):
                        print(col + i[j], end="")
                print()

# -------------------------------------------------------------

def mainUI():
    os.system("cls")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("OPTIONS -- \n\n")
    print("1. One Character")
    print("2. Words (Maximum 15 Letters)")
    print("3. Range (input in Sequence - Max 15 Letters)")
    print("4. Only Alphabets")
    print("5. Only Numbers")
    print("6. Exit")
    print("\n\nEnter Your Choice -- ",end="")

    ch = msv.getch()

    if ch.decode() == "1":
        oneCharacter()
    elif ch.decode() == "2":
        alphaNumWords()
    elif ch.decode() == "3":
        alphaRange()
    elif ch.decode() == "4":
        onlyAlpha()
    elif ch.decode() == "5":
        onlyNum()
    elif ch.decode() == "6":
        return
    
    print("\n\nDo you want to continue Project.. Press y else any key...")
    ch = msv.getch()
    if ch.decode() in ["y", "Y"]:
        mainUI()

mainUI()
