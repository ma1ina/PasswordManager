import csv
def makeFile(PATH):
    with open(PATH, "w") as f:
        linia = csv.writer(f, delimiter=';',quotechar="'")
        linia.writerow(["login","haslo","komentarz"])
