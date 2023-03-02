import time

# def tri_perso(e):
#  return len(e)

def afficher(menu, nbr_pizza=-1):
#  menu.sort(reverse=True, key=tri_perso)
  if nbr_pizza != -1:
    menu = menu[0 : nbr_pizza]
  nb_pizzas = len(menu)

  if nb_pizzas == 0:
    print("----- AUCUNE PIZZA -----")
    return
  
  print(f"----- LISTE DES PIZZAS ({nb_pizzas}) -----")
  for pizza in menu:
    print(pizza)
  print()
  print(f"Première pizza : {menu[0]}")
  print(f"Dernière pizza : {menu[-1]}")


def ajouter(menu):
  new_pizza = input("Ajouter une pizza : ")
  if new_pizza == "":
    return
  if new_pizza.lower() in menu:
    print("Erreur : La pizza existe déjà.\n")
    time.sleep(1)
    return
  menu.append(new_pizza)

pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]

ajouter(pizzas)
afficher(pizzas, 3)