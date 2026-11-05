import math

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        if denominatore == 0:
            raise ValueError("Il denominatore deve essere diverso da zero.")
        else:
            self._denominatore = denominatore
            
    def calcola_fraz(self):
        fraz = self.numeratore / self._denominatore
        return (fraz)
    
    def stampa_fraz(self):
        return(str(self.numeratore) + "/" + str(self._denominatore))
        
    def semplifica_fraz(self):
        mcd = math.gcd(int(self.numeratore), int(self._denominatore))
        self.numeratore = int(self.numeratore // mcd)
        self._denominatore = int(self._denominatore // mcd)
        return(str(self.numeratore) + "/" + str(self._denominatore))
    
    def moltiplica_fraz(self, altra_fraz):
        prod_numeratori = self.numeratore * altra_fraz.numeratore
        prod_denominatori = self._denominatore * altra_fraz._denominatore
        return (str(prod_numeratori) + "/" + str(prod_denominatori))
    
if __name__=="__main__":
    fraz_uno = Frazione(6, 4)
    print(fraz_uno.calcola_fraz())
    print(fraz_uno.stampa_fraz())
    print(fraz_uno.semplifica_fraz())
    fraz_due = Frazione(1, 2)
    print(fraz_uno.moltiplica_fraz(fraz_due))