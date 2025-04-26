loadit = open("config.py",
              "a")
loadit.close()

from config import *
empty = ""
lines = 0


def wrong():
    print("Ungültige Eingabe!")
    auswahl()


def mainloop():
    print("\n\n[0] exit\n[1] create\n[2] load")
    auswahl()


def auswahl():
    entry = str(input("\nAuswahl: "))
    if entry == "0":
        exit()
    elif entry == "1":
        createBtn()
    elif entry == "2":
        load()
    else:
        wrong()


def createBtn():
    global lines
    StrVar = str(input("Name: "))
    if StrVar not in empty:
        lines += 1

        dat = open("config.py",
                   "a")
        dat.write("BtnName" + str(lines) + " = '" + StrVar + "'\n")
        dat.close()
        print(StrVar + " erstellt!")
        mainloop()
    else:
        print("Bitte Zeichen eingeben!")
        createBtn()


def load():
    print("\n\n\n------------------------------------\n")
    with open("config.py", "r") as f:
        for line in f:
            print(line,end="")
    print("\n------------------------------------")
    input("...")
    mainloop()

with open("config.py", "r") as f:
    for line in f:
        lines += 1

mainloop()
