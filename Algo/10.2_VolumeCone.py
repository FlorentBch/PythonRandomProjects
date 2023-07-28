"""

Ecrire l'algorithme qui permet de calculer
le volume d'un cone

Rappel le volume d'un cone 
c'est (pi*rayon²*hauteur)/3


"""
from math import pi
Rayon = int(input("Entrez votre rayon"))
Hauteur = int(input("Entre votre hauteur"))

def formule (rayon,hauteur):
    return pi*((rayon*rayon)*hauteur)/3

print(formule(Rayon,Hauteur))