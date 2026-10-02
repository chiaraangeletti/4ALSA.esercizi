#programma che simuli un piano cartesiano e sia in grado di calcolare la distanza tra due punti.
#verificare se i punti sono posizionati sugli assi, quali nel caso, oppure no.

import math

class Punto:
    def __init__(self,ascissa,ordinata):
        self.ascissa=ascissa
        self.ordinata=ordinata
    def distanzaPunti(self,puntoDue):
        primoTermine = (self.ascissa-puntoDue.ascissa)**2
        secondoTermine = (self.ordinata-puntoDue.ordinata)**2
        distanza = math.sqrt(primoTermine+secondoTermine)
        print (distanza)
    def is_ascissa(self):
        if self.ascissa == 0:
            return True
    def is_ordinata(self):
        if self.ordinata == 0:
            return True

if __name__=="__main__":
    puntoUno=Punto(0,6)
    puntoDue=Punto(3,0)
    puntoUno.distanzaPunti(puntoDue)
    puntoUno.is_ascissa()
    puntoUno.is_ordinata()
    puntoDue.is_ascissa()
    puntoDue.is_ordinata()
    if puntoUno.is_ascissa()==True:
        print("Il punto si trova sull'asse y")
    if puntoUno.is_ordinata()==True:
        print("Il punto si trova sull'asse x")
    if puntoDue.is_ascissa()==True:
        print("Il punto si trova sull'asse y")
    if puntoDue.is_ordinata()==True:
        print("Il punto si trova sull'asse x")