import csv
import os.path
import fileIO

PATH="hasla.dat"


def Main():
    while True:
        try:
            choice=int(input("Podaj liczbe"))

        except ValueError:
            print("to nie jest liczba")
            continue
        else:
            if choice>0:
                if fileExists(PATH):
                    addPassword(PATH,fileIO.data())
                    fileIO.out(PATH,choice)
                else:
                        makeFile(PATH)            
                break
            else:
                print("liczba musi byc wieksza od 0")
                continue



def fileExists(PATH):
    if os.path.exists(PATH):
        return True
    else:
        return False



def addPassword(PATH,dane):
    with open(PATH, "a+", newline="") as f:
        linia = csv.writer(f, delimiter=';',quotechar="'")
        linia.writerow(dane)


def makeFile(PATH):
    with open(PATH, "w") as f:
        linia = csv.writer(f, delimiter=';',quotechar="'")
        linia.writerow(["login","haslo","komentarz"])

if __name__=="__main__":
    Main()