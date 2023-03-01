def conversion(unit1: str, unit2: str, facteur:float):
    value_str = input(f"Conversion {unit1} => {unit2}, Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if value_str == "q":
      return True
    try:
      value_float = float(value_str)
    except ValueError:
       print("Erreur : Vous devez rentrer une valeur numérique")
       print("(utilisez le point et non la virgule pour les décimales)")
       return conversion(unit1, unit2, facteur)
    
    value_convert = round(value_float * facteur, 2)
    print(f"Résultat de la conversion : {value_float} {unit1} = {value_convert} {unit2}")
    return False

while True:
  print("Ce programme vous permet d'effectuer des conversion d'unités")
  print("1 - Pouces vers cm")
  print("2 - cm vers pouces")
  choix = input("Votre choix (1 ou 2): ")
  if choix == "1" or choix == "2":
    break
  print("Erreur : Vous devez choisir 1 ou 2\n")

while True:
  if choix == "1":
    if conversion("pouces", "cm", 2.54):
      break
  if choix == "2":
    if conversion("cm", "pouces", 2.54):
      break