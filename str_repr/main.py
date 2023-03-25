class Personne:
  def __init__(self, nom , age):
    self.nom = nom
    self.age = age

  def Afficher(self):
    print(f"Je m'appelle {self.nom}, j'ai {self.age} ans.")
  
  #représentation chaine de caractère
  #def __str__(self):
   # return str(self.__dict__)
  
  #dev
  def __repr__(self):
    return __class__.__name__ + " " + str(self.__dict__)

personne1 = Personne("Jean", 20)
personne1.Afficher()

print(personne1)