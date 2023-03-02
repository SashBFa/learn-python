# Collections : (Tableaux: Array), Listes, Tuples..
# Tuple (): immutable => non modifiable
# Liste []: mutable => modifiable : rajouter/supprimer des éléments ou les modifier
# Plusieurs éléments


# ---------Tuples------------------
# personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1]) -1 pour le dernier element

# (0,1,2,3,4)
# valeurs = range(0, 5)
# print(valeurs[-1])


# -------------Listes---------------
# personnes = ["Mélanie", "Jean", "Martin", "Alice"]
# nouvelle_personne = "David"

# print(personnes)
# personnes.append(nouvelle_personne) #push
# del personnes[1] #supprimer element
# print(personnes)

"""def modif_valeur(a):
    a[1] = 10
  

test = [1,2,3,4]
print(test)
modif_valeur(test)
print(test)"""

# -------------Fonction et tuples---------------

"""def obtenir_informations():
    return "Mélanie", 37, 1.60

def afficher_informations(nom, age, taille):
    print(f"Informations: Nom : {nom}, Age : {age}, Taille : {taille}")"""

# infos = obtenir_informations()
# print(f"Nom : {infos[0]}")
# print(f"Age : {infos[1]}")
# print(f"Taille : {infos[2]}")

# nom, age, taille = obtenir_informations()
# afficher_informations(nom, age, taille)

# infos = obtenir_informations()
# afficher_informations(*infos) # *info == info[0], info[1], info[2] => unpack tuple

# -------------Slices---------------
"""personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")

for i in personnes[::2]:
  print(i)"""


# -------------Exercices------------

list_person = []

def ask_names():
  name = input("Nouveau nom à ajouter : ")
  if name == "":
    return
  list_person.append(name)
  return ask_names()

ask_names()
print(*list_person)
