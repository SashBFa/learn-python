import random
import time
import os

game_number = ""
score = 0

def clear_screen():
  if(os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')
    
for i in range(0, 4):
  game_number += str(random.randint(0,9))

while True:
  clear_screen()
  print("Retenez la séquence suivant :")
  time.sleep(1)
  print(game_number)
  time.sleep(3)
  clear_screen()
  response = input("Votre réponse : ")
  if response == game_number:
    score += 1
    game_number += str(random.randint(0,9))
    clear_screen()
    print("Bonne réponse")
    print(f"Votre score est de {score}")
    time.sleep(1)
  else:
    break

print("Partie terminée")
print(f"La bonne réponse était : {game_number}")
print(f"Votre score est de {score}")