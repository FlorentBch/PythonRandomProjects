"""
Algorithme pour recherche lineaire:
Cet algo a pour but de chercher trés simplement un element dans 
un tableau et de retourner sa postion.

Il suffit de parcourir un par un les elements d'un tableau
 jusqu'a trouver celui demander.

"""
import random # import de la librairie random pour generer un nombre aléatoire
arr = []

# bout de code pour remplir un tableau de 500 nombres aléatoires compris entre 0 et 1000
for i in range(500):
    arr.append(random.randrange(0,1000))

# élément a trouver
elem = 42
cpt = 0

for i in range (len(arr)):
    cpt+=1
    if arr[i] == elem:
        print(elem," a été trouvé à l'index: ",i,"!")
        break
if cpt == len(arr):
    print("Lélément n'a pas été trouvé :(")