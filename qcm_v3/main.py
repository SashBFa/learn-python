
class Question:

  def __init__(self, title:str, propositions:tuple, answers:str):
    self.title = title
    self.propositions = propositions
    self.answers = answers

  def FromData(data):
    return Question(data)

  def poser(self):
    self.Display()
    return self.propositions[self.Ask_entries() - 1] == self.answers
      
  def Display(self):
    print()
    print(self.title)    
    for i in range(len(self.propositions)):
      print(f"{i + 1} - {self.propositions[i]}")
  
  def Ask_entries(self):
    min, max = 1, len(self.propositions)
    entries_str = input(f"Entrez une réponse entre {min} et {max} : ")
    try:
      entries_int = int(entries_str)
      if entries_int in range(min, max + 1):
        return entries_int
      
      print(f"Erreur: Vous devez rentrer un nombre entre {min} et {max}.")    
    except ValueError:
      print("Erreur: Veuillez rentrer uniquement des chiffres")    
    return self.Ask_entries()  
                
class Questionnaire:
  def __init__(self, questions):
    self.questions = questions
  
  def run(self):
    score = 0
    for question in self.questions:
      if question.poser():
        score +=1
    print(f"Score final: {score} sur {len(self.questions)}")
    return score

questions = (
  Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
  Question("Quelle est la capitale de l'Italie ?", ("Pise", "Rome", "Florence", "Venise"), "Rome"),
  Question("Quelle est la capitale de la Belgique?", ("Bruxelles", "Liege", "Namur", "Anvers"), "Bruxelles"),
  Question("Quelle est la capitale de l'Allemagne ?", ("Hambourg", "Munich", "Berlin", "Cologne"), "Berlin"),
)

Questionnaire(questions).run()