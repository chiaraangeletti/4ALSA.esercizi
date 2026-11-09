class Sostanza:
    NA = 6.022e23
    def __init__(self, nome, formula, massa_molare, massa=0.0):
        if massa_molare <= 0 or massa < 0:
            raise ValueError("Valori non validi.")
        self.nome = nome
        self.formula = formula
        self.__massa_molare = massa_molare
        self.__massa = massa

    @property
    def massa_molare(self):
        return self.__massa_molare

    @property
    def massa(self):
        return self.__massa

    def aggiungi_massa(self, grammi):
        if grammi <= 0:
            raise ValueError("I grammi da aggiungere devono essere maggiori di 0.")
        else:
            self.__massa = self.__massa + grammi
    
    def preleva_massa(self, grammi):
        if grammi <= 0 or grammi > self.__massa:
            raise ValueError("Quantità non valida o superiore alla massa esistente.")
        else:
            self.__massa = self.__massa - grammi
    
    def moli(self):
        return self.__massa / self.__massa_molare
    
    def numero_particelle(self):
        return self.moli() * self.NA
    
    def descrivi(self):
        return str(self.nome) + "(" + str(self.formula) + ", Massa:" + str(self.__massa) + ", Moli:" + str(self.moli()) + ")"


class Elemento(Sostanza):

    def __init__(self, nome, simbolo, numero_atomico, periodo, massa_molare, massa=0.0, periodo_val=1):
        super().__init__(nome, simbolo, massa_molare, massa)
        if numero_atomico < 1 or not (1 <= periodo <= 7) :
            raise ValueError("Dati elemento non validi.")
        self.numero_atomico = numero_atomico
        self.__periodo = periodo
        
    def numero_neutroni(self):
        return round(self.massa_molare) - self.numero_atomico
    
    def descrivi(self):
        return super() .descrivi() + ", Z:" + str(self.numero_atomico) + ", Neutroni:" + str(self.numero_neutroni())


class Composto(Sostanza):

    def __init__(self, nome, formula, massa_molare, tipo_legame, atomi_per_molecola, massa=0.0):
        super().__init__(nome, formula, massa_molare, massa)
        if atomi_per_molecola < 1:
            raise ValueError("Atomi per molecola insufficienti.")
        self.tipo_legame = tipo_legame
        self.__atomi_per_molecola = atomi_per_molecola
        
    def numero_atomi_totali(self):
        return self.numero_particelle() * self.__atomi_per_molecola
    
    def descrivi(self):
        return super() .descrivi() + ", Atomi Totali: " + str(self.numero_atomi_totali())

class Contenitore:

    def __init__(self, nome, capacita_ml, volume_ml=0.0):
        if capacita_ml <= 0 or not (0 <= volume_ml <= capacita_ml):
            raise ValueError("Capacità o volume non validi.")
        self.nome = nome
        self.__capacita_ml = capacita_ml
        self.__volume_ml = volume_ml

    @property
    def capacita_ml(self):
        return self.__capacita_ml

    @property
    def volume_ml(self):
        return self.__volume_ml
    
    def versa(self, ml):
        if ml <= 0 or ml > self.volume_libero():
            raise ValueError("Volume da versare non valido o spazio insufficiente.")
        else:
            self.__volume_ml = self.__volume_ml + ml
    
    def svuota(self):
        self.__volume_ml = 0.0
        return self.__volume_ml

    def volume_libero(self):
        return self.__capacita_ml - self.__volume_ml
    
    def percentuale_riempimento(self):
        return (self.__volume_ml / self.__capacita_ml) * 100
    
    def descrivi(self):
        return str(self.nome) + ": " + str(self.__volume_ml) + "/" + str(self.__capacita_ml) + " mL " + "(" + str(self.percentuale_riempimento()) + "%)"
    
class Becher(Contenitore):

    def __init__(self, nome, capacita_ml, graduazione_ml, ha_beccuccio=True, volume_ml=0.0):
        super().__init__(nome, capacita_ml, volume_ml)
        if graduazione_ml <= 0:
            raise ValueError("Graduazione non valida.")
        self.ha_beccuccio = ha_beccuccio
        self.__graduazione_ml = graduazione_ml
        
    def volume_letto(self):
        return round(self.volume_ml / self.__graduazione_ml) * self.__graduazione_ml
    
    def descrivi(self):
        return super() .descrivi() + ", Graduazione: " + str(self.__graduazione_ml) + ", Volume Letto: " + str(self.volume_letto())


class Matraccio(Contenitore):

    def __init__(self, nome, capacita_ml, incertezza_ml, temperatura_taratura=20.0, volume_ml=0.0):
        super().__init__(nome, capacita_ml, volume_ml)
        if incertezza_ml <= 0:
            raise ValueError("Incertezza non valida.")
        self.temperatura_taratura = temperatura_taratura
        self.__incertezza_ml = incertezza_ml
        
    def riempi_a_tacca(self):
        self._Contenitore__volume_ml = self.capacita_ml
        
    def volume_con_incertezza(self):
        return self.volume_ml, self.__incertezza_ml
    
    def descrivi(self):
        return super() .descrivi() + " Volume con Incertezza: " + str(self.volume_con_incertezza()) + " mL a " + str(self.temperatura_taratura) + " °C"


class Esperimento:

    def __init__(self, titolo, operatore, sostanze = [], contenitori = [], registro = []):
        self.titolo = titolo
        self.operatore = operatore
        self.__sostanze = sostanze
        self.__contenitori = contenitori 
        self.__registro = registro

    def _registra(self, messaggio):
        self.__registro.append(messaggio)
        
    def aggiungi_sostanza(self, sostanza):
        if not isinstance(sostanza, Sostanza):
            raise TypeError("L'oggetto non è una Sostanza valida.")
        if sostanza in self.__sostanze:
            raise ValueError("La sostanza è già presente nell'esperimento.")
        self.__sostanze.append(sostanza)
        self._registra("Aggiunta sostanza: " + str(sostanza.nome))
    
    def aggiungi_contenitore(self, contenitore):
        if not isinstance(contenitore, Contenitore):
            raise TypeError("L'oggetto non è un Contenitore valido.")
        if contenitore in self.__contenitori:
            raise ValueError("Il contenitore è già presente nell'esperimento.")
        self.__contenitori.append(contenitore)
        self._registra("Aggiunto contenitore: " + str(contenitore.nome))
    
    def rimuovi_sostanza(self, sostanza):
        if sostanza not in self.__sostanze:
            raise ValueError("La sostanza non è presente nell'esperimento.")
        self.__sostanze.remove(sostanza)
        self._registra("Rimossa sostanza: " + str(sostanza.nome))
    
    def massa_totale(self):
        totale = 0.0
        for s in self.__sostanze:
            totale = totale + s.massa
        return totale
    
    def moli_totali(self):
        totale = 0.0
        for s in self.__sostanze:
            totale = totale + s.moli()
        return totale
    
    def capacita_totale_ml(self):
        totale = 0.0
        for c in self.__contenitori:
            totale = totale + c.capacita_ml
        return totale
    
    def sostanza_piu_abbondante(self):
        if not self.__sostanze:
            return None
        return max(self.__sostanze, key=lambda s: s.moli())

    def concentrazione_molare(self, sostanza, contenitore):
        if sostanza not in self.__sostanze or contenitore not in self.__contenitori:
            raise ValueError("Sostanza o contenitore non fanno parte dell'esperimento.")
        if contenitore.volume_ml == 0:
            raise ValueError("Il contenitore è vuoto.")
        moli = sostanza.moli()
        litri = contenitore.volume_ml / 1000.0  # conversione ml in litri
        molarita = moli / litri
        self._registra("Calcolata concentrazione per {}: {:.4f} mol/L".format(sostanza.nome, molarita))
        return molarita

    def stampa_registro(self):
        print("--- REGISTRO ESPERIMENTO: " + str(self.titolo) + " ---")
        for i, messaggio in enumerate(self.__registro, start=1):
            print("{}. {}".format(i, messaggio))
            
if __name__ == "__main__":
    print("=== AVVIO TEST LABORATORIO DI CHIMICA ===")
    try:
        # 1. Creazione di un Elemento e di un Composto con massa iniziale
        ferro = Elemento("Ferro", "Fe", 26, 4, 55.845, 100.0)
        cloruro = Composto("Cloruro di sodio", "NaCl", 58.44, "ionico", 2, 50.0)
        
        # 2. Creazione di un Becher e di un Matraccio
        becher = Becher("Becher 250 mL", 250.0, 25.0, ha_beccuccio=True)
        matraccio = Matraccio("Matraccio 100 mL", 100.0, 0.1, temperatura_taratura=20.0)
        
        # 3. Chiamata del metodo descrivi() su tutti e quattro
        print("\n--- TEST DESCRIZIONE ---")
        print(ferro.descrivi())
        print(cloruro.descrivi())
        print(becher.descrivi())
        print(matraccio.descrivi())
        
        # 4. Creazione dell'Esperimento e aggiunta degli oggetti (Aggregazione)
        print("\n--- TEST ESPERIMENTO ---")
        exp = Esperimento("Saggi di Soluzione", "Mario Rossi")
        exp.aggiungi_sostanza(ferro)
        exp.aggiungi_sostanza(cloruro)
        exp.aggiungi_contenitore(becher)
        exp.aggiungi_contenitore(matraccio)
        
        # 5. Calcolo concentrazione molare nel matraccio riempito a tacca
        matraccio.riempi_a_tacca()
        molarita = exp.concentrazione_molare(cloruro, matraccio)
        print("Concentrazione calcolata: {:.4f} mol/L".format(molarita))
        
        # 6. Stampa del registro dell'esperimento
        print()
        exp.stampa_registro()
        
        # 7. Gestione di almeno tre errori con try/except
        print("\n--- TEST GESTIONE ERRORI ---")
        
        # Errore 1: Versare più liquido della capacità del contenitore
        try:
            becher.versa(300.0)
        except ValueError as e:
            print("Errore intercettato 1: {}".format(e))
            
        # Errore 2: Aggiungere un oggetto che non è una Sostanza
        try:
            exp.aggiungi_sostanza("Non sono una sostanza")
        except TypeError as e:
            print("Errore intercettato 2: {}".format(e))
            
        # Errore 3: Creare un Elemento con numero atomico non valido
        try:
            bad_elem = Elemento("Errore", "X", 0, 2, 10.0)
        except ValueError as e:
            print("Errore intercettato 3: {}".format(e))
            
        # 8. Prova dell'aggregazione: gli oggetti esistono ancora fuori dall'esperimento
        print("\n--- VERIFICA AGGREGAZIONE ---")
        print("Il ferro esiste ancora fuori dall'esperimento? Massa: {}g".format(ferro.massa))
        
    except Exception as e:
        print("Errore inatteso durante i test: {}".format(e))