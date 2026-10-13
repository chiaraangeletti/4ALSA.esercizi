#Definizione della classe padre
class Roccia:
    def __init__(self, compMinerale, ciclo, stato):
        self.compMinerale=compMinerale
        self.ciclo=ciclo
        self.stato=stato
        
#Definizione dele classi figlie
class Magmatica(Roccia):
    def __init__(self, compMinerale, ciclo, stato):
        super().__init__(self, compMinerale, ciclo, stato)
    def raffreddamento(self):
        print("La roccia è in fase di raffreddamento")
        
class Sedimentaria(Roccia):
    def __init__(self, compMinerale, ciclo, stato):
        super().__init__(self, compMinerale, ciclo, stato)
    
class Metamorfica(Roccia):
    def __init__(self, compMinerale, ciclo, stato):
        super().__init__(self, compMinerale, ciclo, stato)
    
#Istanziare la classe padre
rocciaGenerica=Roccia("CA", "CICLO A", "FONDAMENTALE")
#Istanziare la classe figlia
rocciaGenerica=Magmatica("CA", "CICLO A", "FONDAMENTALE")
rocciaGenerica.raffreddamento()