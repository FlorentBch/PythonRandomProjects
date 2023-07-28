"""
Permis :

Un permis de chasse à points possède au départ 
un capital de 100 points.

Si le chasseur tire sur (on sait pas si la cible a survecu) :
    - une poule, il perd 1 point,
    - un chien, il perd 3 points,
    - une vache, il perd 5 points,
    - un autre chasseur, il perd 25.

Écrire un script qui  permet de calculer le nombre de point perdus.
sachant qu'un permis coute 200 euros,
calculer en fonction de son tableau de chasse,
le cout déboursé par ce chasseur.

"""

import random

PrixPermis = 200
PointsPermis = 0
Portefeuille = 600

def CreationPermis (permis):
    permis+=100
    return permis


def RetirerPointsPermis (permis, nbrPoints)->int:
    permis-=nbrPoints
    return permis

def RetirerPortefeuille (portefeuille)->int:
    portefeuille -= PrixPermis
    return portefeuille
 
def Tir(NbrTir,NbrPoint, Portefeuille)->str:

    Poule = 1
    Chien = 3
    Vache = 5
    Chasseur = 25
    liste = (1,3,5,25)
    NbrPointUser=NbrPoint
    i=0
    while(i<NbrTir):
            NbrPointUser = RetirerPointsPermis(NbrPointUser,random.choice(liste))
            print(NbrPointUser)
            i+=1
            if NbrPointUser<0:
                print("Points insuffisants, recharge et décompte du portefeuille en cours")
                NbrPointUser = CreationPermis(NbrPointUser)
                Portefeuille = RetirerPortefeuille(Portefeuille)
                print("Points maintenant à ",NbrPointUser, " et le solde est à ",Portefeuille)
                
    return print("Votre nombre de points est égale à ", NbrPointUser, " et votre solde de portefeuille est égale à ", Portefeuille)

NombreTirs = int(input("Quels sont les nombres de tirs effectués ? "))

PointsPermis = CreationPermis(PointsPermis)
Portefeuille = RetirerPortefeuille(Portefeuille)
Tir(NombreTirs,PointsPermis, Portefeuille)

        