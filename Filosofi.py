class Filosofo:
    def __init__(self, nome, anno_nascita):
        self.nome = nome
        self.anno_nascita = anno_nascita
        
    def caratteri(self):
        print("Filosofo: " + self.nome + ", anno di nascita: " + str(self.anno_nascita) + " a.C.")
        
class ScuolaFilosofica:
    def __init__(self, nome, fondatore, epoca, filosofi):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        self._filosofi = []
        
        # Devo fare un controllo perché devo avere almeno 1 oggetto filosofo
        # per costruire la classe ScuolaFilosofica, come scritto nell'UML
        if len(filosofi) < 1:
            raise ValueError("Deve essere presente almeno un filosofo") #il programma da errore se non rispetta la condizione
        else:
            # Verifichiamo uno per uno gli elementi della lista iniziale
            for f in filosofi:
                if self.verifica_filosofo(f):
                    self._filosofi.append(f)
                else:
                    raise TypeError("Errore: uno degli elementi iniziali non è un oggetto Filosofo valido!")
        
    # Nuovo metodo per verificare che l'oggetto sia un filosofo
    def verifica_filosofo(self, oggetto):
        return isinstance(oggetto, Filosofo)
        
    def descrivi(self):
        return ("Scuola: " + self.nome + " Fondatore: " + self.fondatore + " Epoca: " + self.epoca)
    
    def stampa_filosofi(self):
        print("--- Elenco filosofi della scuola " + self.nome + " ---")
        for f in self._filosofi:
            print("- " + f.nome + " (nato nel " + str(f.anno_nascita) + " a.C.)")
        
    def aggiungi_filosofo(self, filosofo):
        # Prima di aggiungerlo alla lista, verifichiamo che sia un filosofo
        if self.verifica_filosofo(filosofo):
            self._filosofi.append(filosofo)
            print("Filosofo " + filosofo.nome + " aggiunto correttamente.")
        else:
            print("Errore: L'elemento inserito non è un'istanza della classe Filosofo.")
        
class Stoicismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, valore_virtu):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.valore_virtu = valore_virtu
        
    def descrivi(self):
        # Override: nella classe figlia sovrascrivo un metodo della classe padre
        base = super().descrivi()
        return base + "\n[Stoicismo] Valore della virtù: " + self.valore_virtu
        
class Epicureismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, tipo_piacere):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.tipo_piacere = tipo_piacere
        
    def descrivi(self):
        # Override: nella classe figlia sovrascrivo un metodo della classe padre
        base = super().descrivi()
        return base + "\n[Epicureismo] Tipo di piacere: " + self.tipo_piacere

if __name__ == "__main__":
    f_epicuro = Filosofo("Epicuro", 341)
    lista_filosofi = [f_epicuro]
    
    scuola_epicurea = Epicureismo("Epicureismo", "Epicuro", "Ellenismo", lista_filosofi, "Piacere catastematico (assenza di dolore)")
    print(scuola_epicurea.descrivi())
    print()
    
    scuola_epicurea.stampa_filosofi()
    print()
    
    # Test di aggiunta di un filosofo valido
    f_lucrezio = Filosofo("Lucrezio", 99)
    scuola_epicurea.aggiungi_filosofo(f_lucrezio)
    
    print()
    # Test di aggiunta di un elemento errato per vedere se funziona il controllo
    scuola_epicurea.aggiungi_filosofo("Non sono un filosofo")
    
    print()
    scuola_epicurea.stampa_filosofi()