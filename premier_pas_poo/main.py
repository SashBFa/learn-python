# Premiers pas en Programmation orientée object

class Personne:
  def __init__(self, nom):
    self.nom = nom
    print(f"Constructeur Personne {nom}")

  def SePresenter(self):
    print(f"Bonjour, je m'appelle {self.nom}")

personne1 = Personne("Jean")
# personne2 = Personne("Paul")

personne1.SePresenter()

