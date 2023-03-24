#Heritage multiple : MULTIPLE-INHERITANCE

class EtreVivant:
  def afficher_infos(self):
    print('Je suis un être vivant')

class Predateur:
  def chasser_et_manger_proie(self):
    print("miam miam")

class Lion(EtreVivant, Predateur):
  def afficher_infos(self):
    print('Je suis un lion')

class Personne(EtreVivant):
  def afficher_infos(self):
    print('Je suis une personne')

Lion().afficher_infos()
Lion().chasser_et_manger_proie()