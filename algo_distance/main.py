# LISTES - ALGO : VALEUR LA PLUS PETITE

driver_and_distance = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4), ("Jean", 0.9), ("Pierre", 7.1), ("Marie", 1.1), ("Maxime", 0.6)]

close_driver = driver_and_distance[0]

for item in driver_and_distance:
  if item[1] < close_driver[1]:
    close_driver = item

print(f"Le conducteur le plus proche est {close_driver[0]} à {close_driver[1]}km") 