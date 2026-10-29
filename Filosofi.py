class Filosofo:
    def __init__(self, nome, anno_nascita):
        self.nome = nome
        self.anno_nascita = anno_nascita
        
    def caratteri(self):
        print ("Filosofo: " + self.nome + ", anno di nascita: " + str(self.anno_nascita) + " a.C.")
        
class ScuolaFilosofica:
    def __init__(self, nome, fondatore, epoca, filosofi):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        #Devo fare un controllo perché devo avere almeno 1 oggetto filosofo
        #per costruire la classe ScuolaFilosofica, come scritto nell'UML
        if len(filosofi) < 1:
            raise ValueError("Deve essere presente almeno un organello") #il programma da errore se non rispetta la condizione
        else:
            self._filosofi = filosofi
        
    def descrivi(self):
        return ("Scuola: " + self.nome + " fondatore: " + self.fondatore + " epoca: " + self.epoca)
    
    def stampa_filosofi(self):
        print("--- Elenco filosofi della scuola " + self.nome + " ---")
        for f in self._filosofi:
            print("- " + f.nome + " (nato nel " + str(f.anno_nascita) + " a.C.)")
        
    def aggiungi_filosofo(self, filosofo):
        self._filosofi.append(filosofi)
        
class Stoicismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, valore_virtu):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.valore_virtu = valore_virtu
        
    def descrivi(self):
        base = super().descrivi()
        return base + "\n[Stoicismo] Valore della virtù: " + self.valore_virtu
        
class Epicureismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, tipo_piacere):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.tipo_piacere = tipo_piacere
        
    def descrivi(self):
        base = super().descrivi()
        return base + "\n[Epicureismo] Tipo di piacere: " + self.tipo_piacere

if __name__=="__main__":
    f_epicuro = Filosofo("Epicuro", 341)
    lista_filosofi = [f_epicuro]
    scuola_epicurea = Epicureismo("Epicureismo", "Epicuro", "Ellenismo", lista_filosofi, "Piacere catastematico (assenza di dolore)")
    print(scuola_epicurea.descrivi())
    scuola_epicurea.stampa_filosofi()
    #Override: nella classe figlia sovrascrivo un metodo della classe padre a condizione che faccia qualcosa di diverso    