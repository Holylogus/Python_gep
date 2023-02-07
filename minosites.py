'''Múzeum neve: Magyar Zene Háza
Látogató neve: Nagy Zoltán
Értékelés (1-20): 16
 
I/B:
Köszönjük az értékelést! 
    A. Kérje be az alábbi adatokat a fenti mintának megfelelően:
múzeum neve, látogató neve és értékelés!  (2p)
    B. A program az adatbekérés után írja ki a következők egyikét: (a mintának megfelelően – 1p)
Ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,20], zárt intervallum értendő):
    • Amennyiben negatív vagy 0 számot adott meg:
“Az értékelés nem lehet negatív vagy 0!”,
    • Amennyiben 20 feletti egész számot adott meg:
“20 pont feletti értékelés nem elfogadható!”
    • Helyes pont-adat esetén:
“Köszönjük az értékelést!”
Feltételezzük, hogy csak egész számokat adnak meg. (4p + 1p)'''

def beeker():
    muzeum_nev = input("Adja meg a múzeum nevét: ")
    latogato_neve = input("Adja meg a nevét: ")
    ertekeles = int(input("Adja meg az értékelést [1:20]: "))
    while ertekeles < 1 or ertekeles > 20:
        if ertekeles < 1:
            print("Az értékelés nem lehet negatív vagy 0!")
            ertekeles = int(input("Adja meg az értékelést [1:20]: "))
        elif ertekeles > 20:
            print("20 pont feletti értékelés nem elfogadható!")
            ertekeles = int(input("Adja meg az értékelést [1:20]: "))
    print("Köszönjük az értékelést!")
    eredmeny = []
    eredmeny.append(muzeum_nev)
    eredmeny.append(latogato_neve)
    eredmeny.append(ertekeles)
    return eredmeny


def kiir(eredmeny):
    print("I/A:")
    print(f"Múzeum neve: {eredmeny[0]}")
    print(f"Látogató neve: {eredmeny[1]}")
    print(f"Értékelés (1-20): {eredmeny[2]}")
