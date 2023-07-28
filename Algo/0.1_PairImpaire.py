"""
Paire ou impaire

Creer un script qui demande un nombre.

le script doit afficher si le nombre est paire ou impaire

"""

nombre = int(input("Quel est votre nombre ?"))

while nombre <1:
    nombre = int("Entrez un nombre supérieur à 1")
    
if nombre %2 ==0:
    print(nombre," est pair.")
else:
    print(nombre," est impaire.")