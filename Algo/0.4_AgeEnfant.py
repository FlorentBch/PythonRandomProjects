"""
    Ecrire un alor qui demande d'entrer l'age d'un enfant et qui vérifie dans quel catégorie il est :
    si >= a 12 -> Cadet
    si >= a 10 -> Minime
    si >= a 8 -> Pupille
    sinon -> Poussin
"""

def DefAge(age):
    Categorie="Poussin"
    if(age>= 12):
        Categorie="Cadet"
    elif(age>=10):
        Categorie="Minime"
    elif(age>=8):
        Categorie="Pupille"
    return Categorie

AgeEnfant = int(input("Quel est votre age ?"))
    
print(DefAge(AgeEnfant))

