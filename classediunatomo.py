#Costruzione di una classe che disegni un atomo
class Atomo:
    def __init__(self, simbolo, numeroAtomico, massa):
        self.simbolo=simbolo
        if numeroAtomico<0:
            raise ValueError("Il numero atomico deve essere positivo") #il programma da errore se non rispetta la condizione
        else:
            self.numeroAtomico=numeroAtomico
        self.massa=massa #gli attributi simbolo, numero Atomico e massa si definiscono pubblici (public), ovvero che vi posso accedere da esterno
        self.__orbitale="2p" #questo attributo è privato e per potervi accedere devo scrivere una funzione anche solo per stamparlo

    def is_stable(self):
        protoni=self.numeroAtomico
        massaDue=round(self.massa)
        neutroni=massaDue-self.numeroAtomico
        rapporto=neutroni/self.numeroAtomico
        if rapporto>=0.9 and rapporto<=1.6:
            print("L'atomo è stabile")
        else:
            print("L'atomo è instabile")

    def print_orbitale(self):
        print(self.__orbitale)

    def new_massa(self):
        

    def new_orbitale(self):
        if self.__orbitale==self.orbitale_camb:
            print("L'orbitale non è cambiato")
        else:
            print("L'orbitale è cambiato")
              
ferro=Atomo("Fe", 26, 55.84)
ferro.is_stable() #molto simile a lista.append() perché la lista e il dizionario sono oggetti
#sintassi per accedere dall'esterno ad un attributo pubblico:
print(ferro.simbolo)
#sintassi per accedere dall'esterno ad un attributo privato dopo aver creato la funzione:
print(ferro.print_orbitale())
try:
    idrogeno=Atomo("H", 1, 1.008)
    idrogeno.is_stable()
except ValueError:
    print("Il numero atomico deve essere positivo")
ferro_camb=input("Inserire la nuova massa del ferro: ")
ferro_camb=float
ferro.new_massa()
orbitaleFe_camb=input("Inserire il nuovo orbitale del ferro: ")
ferro.new_orbitale()
idrogeno_camb=input("Inserire la nuova massa dell'idrogeno: ")
idrogeno_camb=float
idrogeno.new_massa()
orbitaleH_camb=input("Inserire il nuovo orbitale dell'idrogeno: ")
idrogeno.new_orbitale()