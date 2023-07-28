"""
    Ecrire un algo qui demande un nombre entier positif et qui nous retourne le carré de ce nombre
    Un carré est le résultat de la multiplication du nombre par lui même
    On peux pousser un peux et ajouter la vérification de la donnée avec une boucle "while"
"""

NombrePositif = int(input("Entrez votre nombre entier positif svp :"))
while(NombrePositif<1):
    NombrePositif = int(input("Entrez votre nombre entier positif svp :"))
CarreNombre = (NombrePositif * NombrePositif)

i=0
NombreVerif=0
print("\nLa vérification du résultat est le suivant : ")
while i < NombrePositif :
    i+=1
    NombreVerif += NombrePositif
    print("Itération ",i," ->", NombreVerif)

print("Le total est donc le suivant ",CarreNombre)