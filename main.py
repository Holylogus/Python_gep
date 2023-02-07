import minosites
import sorozat
import helyzet

eredmeny = minosites.beeker()
minosites.kiir(eredmeny)
lista = sorozat.vel15()
sorozat.kiir(lista)
tizzel_osthatok = sorozat.oszthato(lista)
sorozat.konzolra_ir(tizzel_osthatok)
sorozat.fajlba_ir("kimutatas.txt", tizzel_osthatok, lista)
osztaly = helyzet.fajlbeolvas()
helyzet.gepek_szama(osztaly)
helyzet.atlag(osztaly)
helyzet.legkisebb(osztaly)