# Premiers pas en Programmation orientée object
class EtreVivant:
  ESPECE_ETRE_VIVANT = "(être vivant non identifié)"  

  def Afficher_type_vivant(self):
    print(f"Type : {self.ESPECE_ETRE_VIVANT}")


class Chat(EtreVivant):
  ESPECE_ETRE_VIVANT = "Chat (Mammifère felin)"


class Personne(EtreVivant):
  ESPECE_ETRE_VIVANT = "Humain (Mammifère homo sapiens)"

  def __init__(self, nom:str = "", age:int = 0):
    self.nom = nom
    self.age = age
    if self.nom == "":
      self.nom = self.DemanderNom()

  def SePresenter(self):
    age_txt = "" if self.age <= 0 else f", j'ai {self.age} ans"
    majeur = "Je suis majeur" if self.EstMajeur() else "Je suis mineur"

    print(f"Bonjour, je m'appelle {self.nom}{age_txt}")
    print(f"{majeur}")

  def EstMajeur(self):
    return self.age >= 18
  
  def DemanderNom(self):
    name = input("Votre nom : ")
    return name

class Etudiant(Personne):
  def __init__(self, nom:str, age:int, etudes:str):
    super().__init__(nom, age)
    self.etudes = etudes

  def SePresenter(self):
    super().SePresenter()
    print(f"Je suis étudiant en {self.etudes}")

liste_personnes = [Personne("Jean", 30), Personne("Paul", 15), Personne("Zoe", 20)]

for personne in liste_personnes:
  personne.SePresenter()
  personne.Afficher_type_vivant()
  print()

chat= Chat()
chat.Afficher_type_vivant()

etudiant = Etudiant("Jean-Michel", 23, "Ecole du cirque")
etudiant.SePresenter()