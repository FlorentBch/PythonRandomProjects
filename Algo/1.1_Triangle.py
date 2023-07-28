"""
Created on Wed Jun 19 10:35:21 2019
"""

"""
Triangle

But de l'exercice :
    
Votre programme demande un nombre positif à 
l'utilisateur.

Il affiche un triangle d'astérisques dont
 la taille dépend du nombre et qui point vers la droite:

Exemple pour le nombre 5 le programme affiche :

*
**
***
****
*****
****
***
**
*
"""


Nombre = int(input("Quel est votre nombre positif ?"))
while(Nombre<=0):
    Nombre = int(input("Quel est votre nombre positif ?"))

i=0
charUp=""
for i in range(Nombre):
    charUp+="*"
    print(charUp)
    
for i in range(Nombre):
    print(((Nombre-i)-1)*"*")
    
