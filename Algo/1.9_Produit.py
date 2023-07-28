"""
    Ecrire un algo qui demande deux nombre a l'utilisateur et qui va vérifier si le produit des deux nombre est positif ou négatif ou nul
    Mais on ne réalise pas le calcul
    
    -Le produit de deux nombres positifs est positif
    -Le produit de deux nombres négatifs est positif
    -Le produit d'un nombre négatif et d'un nombre positif est négatif   
"""
Nombre1 = int(input("Entrez votre 1er nombre : "))
Nombre2 = int(input("Entrez votre 2eme nombre : "))

if(Nombre1>0 and Nombre2>0):
    print("Le produit de deux nombres positifs est positif")
elif(Nombre1<0 and Nombre2<0):
    print("Le produit de deux nombres négatifs est positif")
elif(Nombre1==0 or Nombre2==0):
    print("Le produit de deux nombre comportant un 0 est null")
else:
    print("Le produit d'un nombre négatif et d'un nombre positif est négatif")