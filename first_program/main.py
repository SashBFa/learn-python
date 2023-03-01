"""
Premier programme
Formation Python
On demande le nom et l'age de la personne
"""

def ask_name():
  name_int = ""
  while name_int == "":
    name_int = input('Quel est ton nom ? ')
  return name_int


def ask_age(name_user):
  age_int = 0
  while age_int == 0:
    age_str = input(name_user + ' quel est votre âge ? ')
    try:
      age_int = int(age_str)
    except ValueError:
      print("Erreur: Vous devez rentrer un nombre pour l'âge.")
  return age_int    


def response_prompt(name, age, size=0):
  print()
  # print("Vous vous appelez " + name + ", vous avez " + str(age) + " ans.")
  # print("Vous vous appelez %s, vous avez %s ans" % (name, age))
  print(f"Vous vous appelez {name}, vous avez {age} ans")

  # print("L'an prochain vous aurez " + str(age + 1) + " ans")
  print("L'an prochain vous aurez %s ans" % (age +1))

  if age == 17:
    print("Vous êtes presque majeur")
  elif 12 <= age < 18:
    print('Vous êtes adolescent')
  elif age == 1 or age == 2:
    print("Vous êtes un bébé")
  elif age == 18:
    print("Tout juste majeur : Félicitation")
  elif age > 60:
    print("Vous êtes sénior")
  elif age < 10:
    print("Vous êtes enfant")
  elif age >= 18:
    print("Vous êtes majeur")
  else:
    print("Vous êtes mineur")

  if not size == 0:
    print("Votre taille : " + str(size) + " m")


#name1 = ask_name()
#name2 = ask_name()

#age1 = ask_age(name1)
#age2 = ask_age(name2)

#response_prompt(name1, age1)
#response_prompt(name2, age2)

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
  name = "personne" + str(i+1)
  age = ask_age(name)
  response_prompt(name, age)

"""
n = 0
while n < 4:
    print("Valeur de n: " + str(n))
    n = n + 1

print("Fin de la boucle")

mot_de_passe = ""
while not mot_de_passe == "TOTO":
    mot_de_passe = input("Quel est le mot de passe ? ")

print("Mot de passe correct, vous avez accès au compte")
"""

# print("""
# Vous
#   mettez
#     ce que vous voulez
# """)

# print("toto", 20, "ans", "taille:", 1.80, "m")