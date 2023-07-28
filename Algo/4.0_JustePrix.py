"""
LeJustePrix !

But de l'exercice :
    
Votre programme génère un nombre aléatoire
entre 1 et 1 000.

Il demande ensuite à l'utilisateur de proposer
un nombre.

L'utilisateur entre un nombre dans la console :
    - Si celui-ci est plus petit que le nombre généré, le programme affiche :
    "C'est PLUS !" et demande un nouveau nombre.
    - Si celui-ci est plus grand que le nombre généré, le programme affiche :
    "C'est MOINS !" et demande un nouveau nombre.
    - Si celui-ci est le nombre généré aléatoirement, le programme affiche :
    "C'est GAGNÉ !" puis l'exécution du programme se termine.

Le nombre d'essaie de l'utilisateur est limité à 10 :
    - Chaque tour, le programme affiche le nombre de tours restants à
    l'utilisateur
    - Si au bout de 10 essais l'utilisateur n'a pas trouvé le nombre,
    le programme affiche : "C'est PERDU ! Le nombre était : nombreAleatoire"
    puis l'exécution du programme se termine.

"""

import random

NumeroGagnant = random.randint(1,1000)
Jeu = bool()
Jeu = False
NombreCoups = 10
Proposition = 0

while Jeu == False and NombreCoups>=0:
    Proposition = int(input("Proposition : "))
    if(Proposition==NumeroGagnant):
        Jeu=True
        print("Vous avez réussi en",11-NombreCoups,"coups")
        print("Bravo !!")
    if(Proposition!=NumeroGagnant):
        NombreCoups-=1
        print("Il vous reste",NombreCoups,"coups pour reussir vore coup")
        if(Proposition>NumeroGagnant):
            print("C'est moins !")
        else:
            print("C'est plus !")
    if(NombreCoups==0):
        print("Dommage vous avez perdu :(", "\nLe numéro gagnant était le",NumeroGagnant)