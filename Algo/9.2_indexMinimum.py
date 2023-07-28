"""

Index Minimum:

Ecrir un script qui permet de generer une liste 
de nombres entiers aleatoires,
de taille et de borne définis.


Utiliser la fonction randint(a, b) du module random.

Le script doit permettre de recuperer l'index de l'element le plus petit,
puis de le dépacer en premier position.
"""
import random
liste = []


# remplissage du tableau avec 500 valeurs aléatoires comprisent entre 0 et 1000
for i in range(500):
    liste.append(random.randrange(0, 1000))

for i in range (len(liste)):
    min_index = i
    for j in range(i+1,len(liste)):
        if(liste[j]<liste[min_index]):
            min_index = j
    liste[i], liste[min_index] = liste[min_index], liste[i]
    break
print(min_index)