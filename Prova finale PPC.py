#Parte 1
class Studente:
    def __init__(self, nome, cognome, eta, matricola, CdL, dipartimento):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []
        self.ore = []
        self.CdL = CdL
        self.dipartimento = dipartimento

    def presentati(self):
        return f"Ciao! Sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}; studio {self.CdL} nel {self.dipartimento}."

    def aggiungi_voto(self, voto):
        self.voti.append(voto)
        print(f"Voto {voto} aggiunto a {self.nome}.")

    def calcola_media(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        self.ore.append(ore)
        totale_ore = sum(self.ore)
        print(f"{self.nome} sta studiando da {totale_ore} ore per il suo esame")


#Parte 2
studente1 = Studente("Marco", "Rossi", 20, 201176, "Biotecnologie", "Dipartimento di scienze e tecnologie biologiche ed ambientali")
studente2 = Studente("Giulia", "Bianchi", 22, 200345, "Economia aziendale", "Dipartimento di scienze dell'economia")
studente3 = Studente("Mattia", "Russo", 23, 200821, "Ingegneria civile", "Dipartimento di ingegneria dell'informazione")

#Parte 3
print(studente1.presentati())
studente1.aggiungi_voto(21)
studente1.aggiungi_voto(25)
studente1.aggiungi_voto(22)
studente1.studia(32)
print(f"Media voti di {studente1.nome}: {studente1.calcola_media():.2f}")

print(studente2.presentati())
studente2.aggiungi_voto(28)
studente2.aggiungi_voto(27)
studente2.studia(8)
print(f"Media voti di {studente2.nome}: {studente2.calcola_media():.2f}")

print(studente3.presentati())
studente3.aggiungi_voto(25)
studente3.studia(24)
print(f"Media voti di {studente3.nome}: {studente3.calcola_media():.2f}")

#Parte 4
studente1.aggiungi_voto(18)
studente1.aggiungi_voto(26)
studente1.studia(20)
print(f"Media voti di {studente1.nome}: {studente1.calcola_media():.2f}")

studente2.aggiungi_voto(29)
studente2.studia(12)
print(f"Media voti di {studente2.nome}: {studente2.calcola_media():.2f}")

studente3.aggiungi_voto(30)
studente3.aggiungi_voto(30)
studente3.aggiungi_voto(30)
studente3.studia(40)
print(f"Media voti di {studente3.nome}: {studente3.calcola_media():.2f}")

