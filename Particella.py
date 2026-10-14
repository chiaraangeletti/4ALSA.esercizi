class Particella:
    def __init__(self, nome, massa, carica, spin):
        self.nome=nome
        self.massa=massa
        self.carica=carica
        self.spin=spin
        
    def energia_riposo(self):
        c=3*10**8
        E=self.massa*(c**2)
        return(E)
    
    def info(self):
        print("Nome:", self.nome, "Massa:", self.massa, "Carica:", self.carica, "Spin:", self.spin)
        
    def e_stabile(self):
        if self.nome== "Elettrone" or "Protone" or "Neutrone" or "Fotone":
            return True
    
class Carica(Particella):
    def __init__(self, nome, massa, carica, spin, tipo):
        super().__init__(nome, massa, carica, spin)
        self.tipo=tipo
        
    def forza_coulomb(self, altra_carica, distanza):
        k=9*10**9
        F=k*((self.carica*altra_carica)/(distanza**2))
        return F

class Neutra(Particella):
    def __init__(self, nome, massa, spin):
        super().__init__(nome, massa, 0.0, spin)
        
    def forza_coulomb(self, altra_carica, distanza):
        return 0.0
    
    def stampa_neutra(self):
        print("Particella neutra")
        
particella_generica=Particella("Protone", 1.6, 1.9, "positiva")
particella_generica.info()