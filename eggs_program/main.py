import time
import platform
import winsound

TEMPS_COQUE = 3 * 60
TEMPS_MOLLET = 6 * 60
TEMPS_DUR = 9 * 60

def timer(cuisson:int):
  duree = cuisson

  while duree > 0:
    min = duree//60
    sec = duree-min*60

    if duree == cuisson:
      print("Cuisson en cours ", end="", flush=True)
    else:
      print(f"\nTemps restant : {min:02d}:{sec:02d} ", end="", flush=True) 

    for i in range(10):
      time.sleep(1)
      duree -= 1
      print(".", end="", flush=True)
    
  if platform.system() == "Windows":
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
  print("\nCuisson terminée !")


while True:
  print("Ce programme vous permet de choisir un minuteur pour la cuisson des oeufs")
  print("a - Oeufs à la coque (3 min)")
  print("b - Oeufs mollets (6 min)")
  print("c - Oeufs durs (9 min)")

  choix = input("Votre choix (a, b ou c): ")

  if choix == "a":
    timer(TEMPS_COQUE)
    break
  if choix == "b":
    timer(TEMPS_MOLLET)
    break
  if choix == "c":
    timer(TEMPS_DUR)
    break
  
  print("\nErreur : Vous devez choisir parmis les propositions\n")


