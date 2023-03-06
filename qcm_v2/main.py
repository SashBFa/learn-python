questionnaire = (
  ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
  ("Quelle est la capitale de l'Italie ?", ("Pise", "Rome", "Florence", "Venise"), "Rome"),
  ("Quelle est la capitale de la Belgique?", ("Bruxelles", "Liege", "Namur", "Anvers"), "Bruxelles"),
  ("Quelle est la capitale de l'Allemagne ?", ("Hambourg", "Munich", "Berlin", "Cologne"), "Berlin"),
)

def num_answer(min, max):
  response_str = input(f"Votre réponse (entre {min} et {max}) : ")
  try :
    response_int = int(response_str)
    if min <= response_int <= max:
      return response_int
    
    print(f"Erreur: Vous devez rentrer un nombre entre {min} et {max}.")
  except ValueError:
    print("Erreur: Veuillez rentrer uniquement des chiffres")
  return num_answer(min, max)


def ask_question(question):
  titre, choix, reponse = question[0], question[1], question[2]
  print(f"Question : {titre}")

  for i in range(len(choix)):
    print(f"({i+1}) - {choix[i]}")
  print()

  response_int = num_answer(1, len(choix))
  if choix[response_int-1].lower() == reponse.lower():
    print("Bonne réponse !")
    print()
    return True
  else:
    print("Mauvaise réponse")
  print()
  return False


def run_questions(questionnaire):
  score = 0
  for question in questionnaire:
    if ask_question(question):
      score += 1

  print("Partie terminée")
  print(f"Votre score total est des {score} sur {len(questionnaire)}")


run_questions(questionnaire)
