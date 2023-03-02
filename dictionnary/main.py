"""person = {'name': "Mélanie", 'age': 25, "size": 1.60}
# print(person)
# print(person['name'])
# print(person['age'])

person['name'] = "Claire"
person['post'] = "Développeur"
achats = ("Chocolat", 'Beurre', "Fromage")
person["achats"] = achats

# print(person)

for i in person:
    print(f"clef: {i} - valeur: {person[i]}")"""


personnes = [
  ("Mélanie", 25, 1.6),
  ("Paul", 29, 1.8),
  ("Jacques", 35, 1.75),
  ("Martin", 16, 1.65),
]

def obtenir_informations(nom, liste):
  for i in liste:
    if i[0]==nom:
      return i
  return None

infos = obtenir_informations("Jacques", personnes)
# print(infos)
# ---- Methode lourde car lecture de chaque ligne de la liste

personnes_dict = {
  "Mélanie": (25, 1.6),
  "Paul": (29, 1.8),
  "Jacques": (35, 1.75),
  "Martin": (16, 1.65),
}

infos = personnes_dict.get("Martin")
print(infos)

# ---- Methode plus légère qui va directement chercher la ligne si elle existe