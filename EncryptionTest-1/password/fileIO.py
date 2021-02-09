import csv
def data():
    lhk=[]
    print("Podaj login")
    lhk.append(input())
    print("Podaj haslo")
    lhk.append(input())
    print("Podaj komentarz")
    lhk.append(input())
    return lhk

def out(PATH,choice):
    with open(PATH, "r") as f:
        linia=csv.reader(f, delimiter=';',quotechar="'")
        for i,j in enumerate(linia):
            if i==choice:
                print(j)
