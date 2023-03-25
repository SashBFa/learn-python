class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom
    
    # methode d'instance
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_str(self.nom)} - {self.TYPE}")

    # methode statique
    @staticmethod
    def formater_str(a):
        return a[0].upper() + a[1:].lower()
    
    # methode de classe
    @classmethod
    def methode_de_classe(cls):
        print(f"Méthode de classe : {str(cls.TYPE)}")
    
personne1 = Personne('jean')
personne1.se_presenter()

print(Personne.formater_str("toTo"))

Personne.methode_de_classe()