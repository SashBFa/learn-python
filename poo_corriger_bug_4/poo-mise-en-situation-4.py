# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nbr_personnes = 3
liste_noms = []

for i in range(nbr_personnes):
    nom = input(f"nom de la personne {i+1} : ")
    liste_noms.append(Personne(nom))

for personne in liste_noms:
    personne.SePresenter()