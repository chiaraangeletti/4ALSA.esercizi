import math

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        if denominatore == 0:
            raise ValueError("Il denominatore deve essere diverso da zero.")
        else:
            self.__denominatore = denominatore
            
    def calcola_fraz(self):
        fraz = self.numeratore / self._denominatore
        return (fraz)
    
    def stampa_fraz(self):
        return(self.numeratore + "/" + self._denominatore)
        
    def semplifica_fraz(self):
        mcd = math.gcd(int(self.numeratore), int(self._denominatore))
        self.numeratore = int(self.numeratore // mcd)
        self._denominatore = int(self._denominatore // mcd)
        return(self.numeratore + "/" + self._denominatore)
    
    def moltiplica_fraz(self, frazione):
        prod_numeratori = self.numeratore * frazione.numeratore
        prod_denominatori = self._denominatore * frazione.denominatore
        return (prod_numeratori + "/" + prod_denominatore)