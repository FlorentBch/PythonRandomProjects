"""
pyramide

But de l'exercice :

Reprendre l'exercice 1 Triangle
Votre programme demande un nombre positif à l'utilisateur.
Il affiche un triangle d'astérisques dont la taille dépend du nombre.
Mais cette fois affiché sous forme de pyramide centré

     *
    * *
   * * *
  * * * *
 * * * * *
"""

""" 
Nombre = int(input("Nombre d'étoiles souhaité : "))
if(Nombre>0):
    i=1
    NombreEspace=Nombre
    for i in range(Nombre+1):
        print((NombreEspace)*" ",i*" *")
        NombreEspace-=1
"""


Nombre = int(input("Nombre d'étoiles souhaité : "))
if(Nombre>0):
    i=0
while i <= Nombre:
    print((Nombre-i)*" ", (i*" *"))
    i+=1
    