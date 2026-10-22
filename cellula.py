class Organello:
    def __init__(self, nome, efficienza, energia_base):
        self.nome = nome
        self.efficienza = efficienza
        self.energia_base = energia_base
        
class Cellula:
    def __init__(self, intatto, nome, forma, membrana, dimensione, organelli, tipo_nutrizione):
        self.intatto = intatto
        #Devo fare un controllo perché devo avere almeno 1 oggetto organello
        #per costruire la classe Cellula, come scritto nell'UML
        if len(organelli) < 1:
            raise ValueError("Deve essere presente almeno un organello") #il programma da errore se non rispetta la condizione
        else:
            self._organelli = organelli
        self.nome = nome
        self.forma = forma
        self._membrana = membrana
        self.dimensione = dimensione
        self._organelli = organelli
        self.tipo_nutrizione = tipo_nutrizione
        
    def numero_organelli(self):
        return len(self._organelli)
    
    def aggiungi_organello(self, organello):
        self._organelli.append(organello)
        
class Animale(Cellula):
    def __init__(self, intatto, nome, forma, membrana, dimensione, organelli, tipo_nutrizione, centrioli):
        super().__init__(intatto, nome, forma, membrana, dimensione, organelli, tipo_nutrizione)
        self.centrioli = centrioli
        
class Vegetale(Cellula):
    def __init__(self, intatto, nome, forma, membrana, dimensione, organelli, tipo_nutrizione, spessore_parete):
        super().__init__(intatto, nome, forma, membrana, dimensione, organelli, tipo_nutrizione)
        self.spessore_parete = spessore_parete

if __name__=="__main__":
    lista_organelli = []
    mitocondrio = Organello ("Mitocondrio", 0.95, 190)
    lista_organelli.append(mitocondrio)
    cellulaGenerica = Cellula(True, "AK23", "Cerchio", True, 2, lista_organelli, "Vegano")
    print(cellulaGenerica.numero_organelli())
    #Override: nella classe figlia sovrascrivo un metodo della classe padre a condizione che faccia qualcosa di diverso    