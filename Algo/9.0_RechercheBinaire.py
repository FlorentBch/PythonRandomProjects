"""
Recherche binaire:

Cet algorithme de recherche est un peu plus compliqué 
mais plus performant que la recherche linéaire
car au pire des cas on ne cherchera que dans la moitié du tableau

Il n'est utilisable qu'avec des tableaux triés.

Le principe est de comparer l'élément à trouver avec l'élément 
au milieu du tableau:

    si le milieu du tableau est inférieur à l'element a trouver
     on divise le tableau en 2 et on répéte la recherche 
     sur cette moitié du tableau
    si le milieu du tableau est supérieur à l'element a trouver 
    on divise le tableau en 2 et on répéte la recherche sur cette moitié 
    du tableau

C'est un cas typique d'utilisation de la récursivité

"""
import random

arr = []
elem = 42    # element a trouver dans le tableau


# remplissage du tableau avec 500 valeurs aléatoires comprisent entre 0 et 1000
for i in range(500):
    arr.append(random.randrange(0, 1000))

# fonction de tri de python
arr.sort()
trouve = False
# Fonction de recherche binaire, elle prend en paramètre l'élément a trouver,
# le tableau dans lequel chercher, et les indice du début et de la fin du tableau.

def binarySearch (find, tbl, start, end):
    trouve = False
    if tbl[len(tbl)//2] == find:
        trouve = True
    elif tbl[len(tbl)//2] > find:
        start = 0
        end = len(tbl)//2
        for i in range (len(tbl)//2):
            del tbl[end]
    else:
        start = len(tbl)//2
        end = len(tbl)
        for i in range (len(tbl)//2):
            del tbl[0]
     
    if (len(tbl)==1):
        print("Aucun élément trouvé dans le tableau")    
    elif trouve == False :
        binarySearch(find,tbl,start,end)
    else :
        print("42, j'en était sûr !")

binarySearch(elem, arr, 0,len(arr))