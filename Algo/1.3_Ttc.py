"""

Calcul d'un prix TTC.

Creer un script qui demande le prix hors taxe
d'un article.
Pus qui demande si l'article est de la nourriture
ou non.
Le script doit calculer le prix ttc selon si
c'est de la nourriture ou non.

rappel, pour les biens communs la TVA c'est 20.0%
sinon c'est 5.5% pour la nourriture

"""

PrixHT =float(input("Quel est le prix Hors taxes ? : "))
BoolNourriture = str(input("Est-ce de la nourriture ? O/ N : "))
PrixTTC=0

if(BoolNourriture=="O" or BoolNourriture=="o"):
    BoolNourriture=True
else:
    BoolNourriture=False
    
if(BoolNourriture==True):
    PrixTTC =PrixHT+(PrixHT*0.055)
    print(PrixTTC)
    
elif(BoolNourriture==False):
    
    PrixTTC = PrixHT+(PrixHT*0.2)
    print(PrixTTC)