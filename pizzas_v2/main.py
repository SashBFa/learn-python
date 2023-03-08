#nom, prix, ingrédients, végétarienne

class Pizza:
  def __init__(self, name:str, price:float, ingredients:tuple, vegetarian:bool=False):
    self.name = name
    self.price = price
    self.ingredients = ingredients
    self.vegetarian = vegetarian
  
  def Display(self):
    veg_str = "- Végétarienne" if self.vegetarian else ""

    print()
    print(f"Pizza {self.name} : {self.price}€ {veg_str}")
    print(" - ".join(self.ingredients))

class CustomPizza(Pizza):
  BASE_PRICE = 8
  PRICE_BY_INGREDIENT = 1.2
  LAST_ID = 0

  def __init__(self):
    CustomPizza.LAST_ID += 1
    super().__init__(f"Personnalisée {self.LAST_ID}", 9, [])
    self.user_ingredients()
    self.price = self.custom_price()
  
  def user_ingredients(self):
    print()
    print(f"Ingrédients pour la pizza personnalisée {self.LAST_ID}")
    while True:
      ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
      if ingredient == "":
        return
      self.ingredients.append(ingredient)
      print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")
  
  def custom_price(self):
      return self.BASE_PRICE + len(self.ingredients) * self.PRICE_BY_INGREDIENT

list_pizzas = [
  Pizza("Margherita", 8, ("tomate", "mozzarella"), True),
  Pizza("Calzone", 10, ("tomate", "mozzarella", "jambon", "champignon", "oeuf", "repliée")),
  Pizza("Roma", 11, ("aubergines", "poivrons", "gorgonzola", "parmesan"), True),
  Pizza("Végétarienne", 11.5, ("poivron", "aubergines", "oignons", "champignons", "courgettes", "épinards"), True),
  Pizza("4 fromages", 10, ("gorgonzola", "mozzarella", "chêvre", "parmesan"),True),
  Pizza("Tartiflette", 12.5, ("reblochon", "pomme de terre", "lardons", "crème")),
  CustomPizza(),
  CustomPizza()
]

for p in list_pizzas:
  p.Display()