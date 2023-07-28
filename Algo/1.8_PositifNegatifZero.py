"""
    Ecrire un algo qui demande un nombre a l'utilisateur et qui va vérifier si ce nombre est positif ou négatif ou nul
    
"""

Nombre = int(input("Entrez votre nombre : "))

if(Nombre>0):
    print("Nombre positif")
elif(Nombre==0):
    print("Nombre nul")
else:
    print("Nombre négatif")