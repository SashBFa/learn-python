import random

MIN_NBR = 1
MAX_NBR = 10
QUESTION_NBR = 4

score = 0


def ask_question():
  a = random.randint(MIN_NBR, MAX_NBR)
  b = random.randint(MIN_NBR, MAX_NBR)
  o = random.randint(0,3)
  nbr_int = 0

  operateur_str = "+"
  calcul = a + b
  
  if o == 1:
    operateur_str = "*"
    calcul = a * b
  elif o == 2:
    operateur_str = "-"
    calcul = a - b
  elif o == 3:
    operateur_str = "/"
    calcul = a / b
  
  while nbr_int == 0:
    nbr_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    try:
      nbr_int = int(nbr_str)
    except ValueError:
      print("Erreur: Vous devez rentrer un nombre. Réessayez. ")
  if nbr_int == calcul:
    return True
  return False


for i in range(0, QUESTION_NBR):
  print(f"Question n°{i+1} sur {QUESTION_NBR}:")
  if ask_question():
    print("Réponse correcte")
    score += 1
  else:
    print("Réponse incorrecte")
  print()

print(f"Votre score est de {score} / {QUESTION_NBR}")

if score == QUESTION_NBR:
  print("Excellent")
elif score == 0:
  print("Révisez vos maths!")
elif score > int(QUESTION_NBR/2):
  print("Pas mal")
else:
  print("Peut mieux faire")