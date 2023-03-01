
POUCE_FACT = 2.54
CM_FACT = 0.394

entry = ""
output = ""

def ask_way():
  way = ""
  while not (way == "A" or way == "B"):
    print()
    way = input("""Veuillez choisir le sens de way :
    - A : pouces vers cm
    - B : cm vers pouces
    Choix : """)
    if not (way == "A" or way == "B"):
      print("Votre réponse ne correspond à aucun choix proposé. Réessayez.")
  return way

line = ask_way()

if line == "A":
  entry = "pouces"
  output = "cm"
elif line == "B":
  entry = "cm"
  output= "pouces"

def ask_value():
  value_float = 0
  while value_float == 0:
    print()
    print("Pour quitter le convertisseur, pressez X.")
    value_str = input(f"Veuillez entrer la valeur en {entry} à convertir en {output} : ")
    if value_str == "X":
      value_float = "X"
      break
    else:
      try:
        value_float = float(value_str)
      except ValueError:
        print()
        print("Erreur: Vous devez rentrer un nombre pour la conversion.")
  return value_float


value_conversion = ask_value()
while not value_conversion == "X":
  value_output = 0
  if entry == "cm":
    value_output = value_conversion * CM_FACT
  elif entry == "pouces":
    value_output = value_conversion * POUCE_FACT
  print()
  print(f"{round(value_conversion,2)} {entry} représente {round(value_output,2)} {output}.")
  value_conversion = ask_value()
