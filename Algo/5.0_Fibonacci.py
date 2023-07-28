"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2

Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)

ex: 
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610
"""

liste = list()
cpt = 2

# liste.append(0)
# liste.append(1)
# while 1:
#     Un = liste[cpt-1] + liste[cpt-2]
#     cpt+=1
#     liste.append(Un)
#     print(Un,"\n")
    
liste = list()
liste.append(0)
liste.append(1)
   
def fibonacci():
    
        un = liste[len(liste)-1] + liste[len(liste)-2]
        liste.append(un)
        print(un,"\n")
        if(len(liste)<100):
            fibonacci()
        
fibonacci()