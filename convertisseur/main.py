
POUCE_FACT = 2.54
CM_FACT = 0.394

def ask_conversion():
  conversion = ""
  while not conversion == "A" or conversion == "B":
    conversion = input("""Veuillez choisir le sens de conversion :
    - A : pouces vers cm
    - B : cm vers pouces
    Choix : """)
  return conversion

ask_conversion()