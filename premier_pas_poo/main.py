# Premiers pas en Programmation orientée object

class Personne:
  def __init__(self, nom:str = "", age:int = 0):
    self.nom = nom
    self.age = age
    if self.nom == "":
      self.nom = self.DemanderNom()

  def SePresenter(self):
    info_personne = f"Bonjour, je m'appelle {self.nom}"

    if self.age <= 0:
      print(info_personne)
      return
    print(f"{info_personne}, j'ai {self.age} ans")

    if self.EstMajeur():
      print("Je suis majeur")
    else:
      print("Je suis mineur")

  def EstMajeur(self):
    return self.age >= 18
  
  def DemanderNom(self):
    name = input("Votre nom : ")
    return name

liste_personnes = [Personne("Jean", 30), Personne("Paul", 15), Personne()]

liste_personnes.append(Personne('Toto', 10))

for personne in liste_personnes:
  personne.SePresenter()

