#
"""
    Ecrire un programme de tri a bulle:

    Le principe du tri a bulle est de comparer un element d'un tableau 
    avec son voisin suivant,
    si l'element est plus grand que son voisin, on inverse les positions
    sinon passe à l'élément suivant
    Astuce :
        Au lieu de passer par une variable temporaire
        python permet de swap:
            liste[i], liste[i+1] = liste[i+1], liste[i]

"""
#

Liste = [8 , 5 , 1 , 7 , 6 , 4]


for i in range (len(Liste)):
    for k in range(len(Liste)):
        if(Liste[i]<Liste[k]):
            Liste[i], Liste[k] = Liste[k], Liste[i]
print(Liste)

# for i in range (len(Liste)):
#     for x in range (len(Liste)):
#         if(Liste[i]<Liste[i+1]):
#             Liste[i], Liste[i+1] = Liste[i+1], Liste[i]
print(Liste)