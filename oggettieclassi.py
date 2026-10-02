#Programma che gestisce nome, cognome, età di due persone

#nome_prima="Tommaso"
#cognome_prima="STRA"
#eta_prima=25

#nome_seconda="Luigi"
#cognome_seconda="Rossi"
#eta_seconda=28

#print("Età prima persona")
#print(eta_prima)
#print("Età seconda persona")
#print(eta_seconda)

#Uso degli oggetti

class Persona:
    def __init__(self, nome, cognome, eta, lavoro): #questo è un costruttore perché inizializza con "init"
        self.nome=nome
        self.cognome=cognome
        self.eta=eta #questi si chiamano attributi e hanno sempre "self." davanti. sono variabili
        self.lavoro=lavoro
    def stampaEta(self):
        print(self.eta)
        if self.eta>=18:
            print("Maggiorenne")
        else:
            print("Minorenne")
    def stampaLavoro(self):
        print(self.lavoro)
        
prima_persona=Persona("Tommaso", "STRA", 16, "Studente")
seconda_persona=Persona("Luigi", "Rossi", 28, "Insegnante") #queste sono istanze
prima_persona.stampaEta()
seconda_persona.stampaEta()
prima_persona.stampaLavoro()
seconda_persona.stampaLavoro()