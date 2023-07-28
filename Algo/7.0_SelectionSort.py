#
"""
    Ecrire un programme de tri par selection:

    Le tri par selection a pour principe de chercher l'element le plus petit
     d'un tableau puis de le placer au debut du tableau

    par exemple:

    tableau de depart: 8 , 5 , 1 , 7 , 6 , 4

    premiere iteration: 1 , 5 , 8 , 7 , 6 , 4

    deuxieme iteration: 1 , 4 , 8 , 7 , 6 , 5

    troisieme iteration: 1 , 4 , 5 , 7 , 6 , 8

    quatrieme iteration: 1 , 4 , 5 , 6 , 7 , 8

    cinquieme iteration: le tableau est dans l'ordre fin du tri

"""
#

liste = [8 , 5 , 1 , 7 , 6 , 4]
cpt=0
for i in range (len(liste)):
    min_index = i
    for j in range(i+1,len(liste)):
        if(liste[j]<liste[min_index]):
            min_index = j
    liste[i], liste[min_index] = liste[min_index], liste[i]
print(liste)

liste = [8 , 5 , 1 , 7 , 6 , 4]
varTemp = 0
listeTemp = list()
for i in range (len(liste)):
    varTemp = min(liste)
    listeTemp.append(varTemp)
    liste.remove(varTemp)
    
print(listeTemp)