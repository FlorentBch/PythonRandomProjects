"""

Suite100

Creer un script qui demande une suite
de nombres positifs ou nuls.

calculez la somme de cette suite
à chaque nombre ajouté.
Comptez combien il y avait de données et
combien étaient supérieures à 100.

afficher le resultat et continer.

Entrer un nombre inférieur à 0 indique la fin de la suite.
"""


Liste = list()
BoolAction = 1
Total=0
NombreSup100=0

while(BoolAction!="0"):
    Input = int(input("Entrez votre nombre positif ou nul : "))
    Liste.append(Input)
    Total+=Input
    print("Le total est égal à ",Total)
    print("Il y a ",len(Liste)," dans votre liste")
    for x in range(len(Liste)):
        if(Liste[x]>=100):
            NombreSup100+=1
    print("Il y a ",NombreSup100," élément(s) supérieur à 100")
    NombreSup100=0
    BoolAction = (input("Voulez vous continuer ? 0/1"))


print(Liste)