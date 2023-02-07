import random

'''II/A, B, C:
 20*-28*124*166*15*-188*174*243*20*28*-124*166*15*-188*174
II/D, E:
           	Tízzel osztható számok száma: 1.  	
kimutatas.txt tartalma:
II/F:
Tízzel osztható számok száma: 1. 
    A. Írasson ki a konzolra csillag jellel (*) 
    elválasztva 15 számból álló véletlen számsorozatot 
    [-90,500] zárt intervallumon a mintának megfelelően! (4p)
    B. A generált értékeket tárolja lista adatszerkezetben!(1p)
    C. A * jel csak az értékek között szerepeljen (a végén,
     elején ne)! (2p)
    D. Írjon függvényt oszthatoak_szama néven, 
    amiben számolja meg, hogy hány olyan elem van, 
    ami tízzel osztható. A visszatérési érték legyen 
    egy egész szám, a függvény bemenete a lista! (3p)
    E. Az oszthatoak_szama függvény eredményét írassa ki 
    a mintának megfelelően a konzolra, amit konzolra_ir 
    nevű metódusban fogalmazzon meg! (2p)
    F. Az oszthatoak_szama függvény eredményét írassa ki 
    a mintának megfelelően a kimutatas.txt nevű fájlba, 
    amit fajl_ir nevű metódusban fogalmazzon meg! (2p)'''

def vel15():
    sorozat = []
    i = 0
    while i < 15:
        sorozat.append(int(random.random()*590-90))
        i += 1
    return sorozat

def kiir(sorozat):
    szoveg = ""
    i = 0
    while i < len(sorozat)-1:
        szoveg += str(sorozat[i]) + "*"
        i += 1
    szoveg += str(sorozat[i])
    print("II/A, B, C:")
    print((szoveg))

def oszthato(sorozat):
    i = 0
    oszthato_szama = 0
    while i < len((sorozat)):
        if sorozat[i] %10 == 0:
            oszthato_szama += 1
            i += 1
        else:
            i += 1
    return oszthato_szama

def konzolra_ir(darab):
    print("II/F:")
    print(f"Tízzel osztható számok száma: {darab}")

def fajlba_ir(fajlnev, darab, sorozat):
    fajl = open(fajlnev, "w", encoding="UTF-8")
    fajl.write("II/F:\n")
    fajl.write(f"Tízzel osztható számok száma: {darab}")

