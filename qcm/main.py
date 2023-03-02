import time
import os

def clear_screen():
  if(os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')


class Questions:
  def __init__(self, q, a, b, c, d, r):
    self.question = q
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.response = r

question1 = Questions("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
question2 = Questions("Quelle est la capitale de l'Italie ?", "Pise", "Rome", "Florence", "Venise", "b")
question3 = Questions("Quelle est la capitale de la Belgique?", "Bruxelles", "Liege", "Namur", "Anvers", "a")
question4 = Questions("Quelle est la capitale de l'Allemagne ?", "Hambourg", "Munich", "Berlin", "Cologne", "c")

questions_list = [question1, question2, question3, question4]
score = 0

clear_screen()
print("Bienvenue dans le questionnaire des capitales.\n")
time.sleep(2)

for i in questions_list:
  clear_screen()
  response =""
  print(f"Question : {i.question}")
  print(f"(a) {i.a}")
  print(f"(b) {i.b}")
  print(f"(c) {i.c}")
  print(f"(d) {i.d}")
  while response != "a" or response != "b" or response != "c" or response != "d":
    response = input("\nVotre réponse : ")
    if response == "a" or response == "b" or response == "c" or response == "d":
      break
    else:
      print("Erreur : Veuillez entrer a, b, c ou d uniquement.")
  if response == i.response:
    score += 1
    print("Bonne réponse !")
    print(f"Votre score est de {score}")
    time.sleep(2)
  else :
    print("Mauvaise réponse")
    print(f"Votre score est de {score}")
    time.sleep(2)

clear_screen()
print("Partie terminée")
print(f"Votre score total est des {score} sur {len(questions_list)}")