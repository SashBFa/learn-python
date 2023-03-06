# Faire un "in" sans prendre en compte la casse
"""
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

def element_dans_liste(el, list):
  return any([nom for nom in list[:] if nom.lower() == el.lower()])

if element_dans_liste("JeAn", noms):
  print("Le prénom existe")
else:
  print("Le prénom n'existe pas")
  
"""

# Extraire les extensions

"""

fichiers = ("notepad.exe", "nom.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (
  ("exe", "Executable"),
  ("doc", "Document Word"),
  ("txt", "Document texte"),
  ("jpeg", "Image JPEG")
)

def extract_extentions(fichier, list):
  clean_fichier = fichier.split(".")
  
  if not len(clean_fichier) > 1:
    print(f"{fichier} (Aucune extension)")
  else:
    definition = [nom[1] for nom in list if clean_fichier[-1].lower() == nom[0].lower()]
    if len(definition) == 0:
      print(f"{fichier} (Extension non connue)")
    else :
      print(f"{fichier} ({definition[0]})")

for fichier in fichiers:
    extract_extentions(fichier, definition_extensions)

"""

# Nombre total de caractères

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

"""
total_caract = 0
for nom in noms:
    total_caract += len(nom)
"""

# total_caract = sum([len(nom) for nom in noms])

total_caract = len("".join(noms))

print(f"Nombre total de caractères : {total_caract}")