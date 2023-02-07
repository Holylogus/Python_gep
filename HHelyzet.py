
'''id (azonosító): pl: 1
·         hely (terem azonosítója): pl.: T403
·         típus (a gép típusát jelöli): pl.: asztali
·         ipcim (a gép ipcíme): pl.: 192.168.2.1'''

class Helyzet:
    def __init__(self, sor):
        self.id = int(sor[0])
        self.hely = sor[1]
        self.tipus = sor[2]
        self.ipcim = sor[3]