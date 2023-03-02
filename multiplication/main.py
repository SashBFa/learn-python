def afficher_table_multiplication(n, min=1, max=10):
  if min >= max:
    print(f"Erreur: la valeur min est supérieur ou égal à la valeur max")
    return
  for i in range(min, max + 1):
    print(f"{i} x {n} = {i*n}")

afficher_table_multiplication(4)