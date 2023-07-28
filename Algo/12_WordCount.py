"""

    écrire l'algorithme qui permet de compter le nombre de mots présents dans une phrase

"""

phrase = input("Entre votre phrase")

tblMots = phrase.split()
cpt = 0

for i in range(len(tblMots)):
    if(tblMots[i] != " "):
        cpt+=1
print(cpt)
        
    