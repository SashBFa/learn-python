# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nbr_personnes = 4
noms = []

for i in range(nbr_personnes):
    nom = input(f"nom de la personne {i+1} : ")
    noms.append(Personne(nom))

for personne in noms:
    personne.SePresenter()