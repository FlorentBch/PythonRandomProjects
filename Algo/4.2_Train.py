"""
Train :

Un train est parti de la gare du Nord à 9 h
(il y a 170 km entre la gare du Nord et Arras).

Écrire un script qui affiche un tableau me permettant de connaître
l'heure à laquelle le train passe à Arras.

Le tableau prédira les différentes heures possibles:
pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h,
les résultats étant arrondis à la minute inférieure.

Écrire une fonction tchoutchou qui reçoit la vitesse du train et
qui affiche l'heure du passage;

Écrire le programme principal qui affiche le tableau demandé.

"""
import math

Distance = 170
Tableau = list()

def tchoutchou (vitesse)-> str:
    NombreTotal = Distance*60/vitesse
    NombreHeures = NombreTotal/60
    NombreHeures = math.floor(NombreHeures)
    NombreMinutes = NombreTotal-NombreHeures*60
    
    heure = str(str((9+NombreHeures))+"h"+str(int(NombreMinutes)))
    return heure

def main():
    for x in range (100,310,10):
        Tableau.append(str(str(x)+"->"+str(tchoutchou(x))))
    print(Tableau)

main()