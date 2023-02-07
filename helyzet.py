from HHelyzet import Helyzet

'''A gep.txt forrásállomány, gépek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         id (azonosító): pl: 1
·         hely (terem azonosítója): pl.: T403
·         típus (a gép típusát jelöli): pl.: asztali
·         ipcim (a gép ipcíme): pl.: 192.168.2.1
Az állomány első sora a mezőneveket tartalmazza felkiáltó jellel elválasztva.
A megoldás mintája:
III/A, B:
            	A gépek száma: 76.
III/C:
           A páros teremszámú termek azonosító átlaga: 39.
III/D:
            	A legkisebb asztali gép azonosítója: 1, helye: T403.
    A. Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gep.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
    B. Írassa ki a gépek számát a mintának megfelelően a konzolra! A metódus neve legyen gepek_szama! (2p)
    C. Határozza meg és írassa ki a konzolra a minta szerint, hogy a páros teremszámú termeknek mi az azonosító átlaga. A metódus neve legyen atlag! (4p)
    D. Írassa ki konzolra a mintának megfelelően a legkisebb azonosítójú asztali gép azonosítóját és helyét (ha több is van, akkor az első legkisebb adatait). A metódus neve legyen legkisebb!  (4p)'''

def fajlbeolvas():
    fajl = open("gep.txt", "r", encoding="UTF-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    gepek_lista = []

    i = 0
    while i <len(sorok):
        sor = sorok[i].strip().split("!")
        gepek_lista.append(Helyzet(sor))
        i += 1
    return gepek_lista

def gepek_szama(lista):
    print("III/A, B:")
    print(f"A gépek száma: {len(lista)}")

def atlag(lista):
    osszesen = 0
    darab = 0
    i = 0
    while i < len(lista):
        if lista[i].id %2 == 0:
            osszesen += lista[i].id
            darab += 1
            i += 1
        else:
            i += 1

    print("III/C:")
    print(f"A páros teremszámú termek azonosító átlaga: {osszesen/darab}")


def legkisebb(lista):
    i = 0
    minimum_elem = lista[0].id
    while i < len(lista):
        if lista[i].id < minimum_elem:
            minimum_elem = lista[i].id
            i += 1
        else:
            i += 1
    print("III/D:")
    print(f"A legkisebb asztali gép azonosítója: {lista[0].id}, helye: {lista[0].hely}")