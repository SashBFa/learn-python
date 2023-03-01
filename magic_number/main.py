import random

MIN_NBR = 1
MAX_NBR = 10
MAGIC_NBR = random.randint(MIN_NBR, MAX_NBR)
LIFES_NBR = 4

response = 0
life = LIFES_NBR

def ask_nbr(min, max):
  nbr_int = 0
  while nbr_int == 0:
    nbr_str = input(f"Quel est le nombre magique (entre {min} et {max}) ? ")
    try:
      nbr_int = int(nbr_str)
    except ValueError:
      print("Erreur: Vous devez rentrer un nombre. Réessayez. ")
    else:
       if nbr_int < min or nbr_int > max:
          print(f"Erreur: Le nombre doit être entre {min} et {max}. Réessayez. ")
          nbr_int = 0
  return nbr_int

"""
while not response == MAGIC_NBR and life > 0:
  print(f"Nombre de vie restant : {life}")
  response = ask_nbr(MIN_NBR, MAX_NBR)
  if response < MAGIC_NBR:
    print("Le nombre magique est plus grand")
    life -= 1
  elif response > MAGIC_NBR:
    print("Le nombre magique est plus petit")
    life -= 1
  else : 
    print('Bravo, vous avez trouvé !')

if life == 0:
  print("Vous avez perdu")
"""

endgame = False

for i in range(0, LIFES_NBR):
  vies = LIFES_NBR -i
  print(f"Nombre de vie restant : {vies}")
  response = ask_nbr(MIN_NBR, MAX_NBR)
  if response < MAGIC_NBR:
    print("Le nombre magique est plus grand")
  elif response > MAGIC_NBR:
    print("Le nombre magique est plus petit")
  else : 
    print('Bravo, vous avez trouvé !')
    endgame = True
    break

if not endgame:
  print("Vous avez perdu")