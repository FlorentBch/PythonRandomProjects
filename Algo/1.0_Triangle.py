"""
Created on Wed Jun 19 10:35:21 2019
"""

"""
Triangle

But de l'exercice :
    
Votre programme demande un nombre positif à 
l'utilisateur.

Il affiche un triangle d'astérisques dont
 la taille dépend du nombre :

Exemple pour le nombre 5 le programme affiche :

*
**
***
****
*****
"""


Nombre = int(input("Nombre d'étoiles souhaité : "))
if(Nombre>0):
    i=0
    char="*"
    for i in range(Nombre):
        print(char)
        char+="*"
