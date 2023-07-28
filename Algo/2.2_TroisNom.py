"""
    Ecrire un algo qui demande 3 variable de type String qui sont des noms et qui va vérifier si il sont entrée dans l'ordre alphabétique
    On pourrait pousser l'exercice plus loin en triant les nom si il ne le sont pas de base 
"""
ListeNoms = list()

for x in range (10):
    ListeNoms.append(str(input("Entre ton nom ")))
             
for i in range (len(ListeNoms)):
    for k in range(len(ListeNoms)):
        if(ListeNoms[i]<ListeNoms[k]):
            varTempo = ListeNoms[i]
            ListeNoms[i] = ListeNoms[k]
            ListeNoms[k] = varTempo
      
print(ListeNoms)