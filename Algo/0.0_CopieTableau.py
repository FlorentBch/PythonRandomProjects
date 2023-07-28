import copy
L1=[3,2]
L2=L1 #Ca copie en gardant le même espace mémoire, L1 et L2 sont liée et les changement de L1 = changement sur L2
L2=L1.copy() #Ca copie mais alloue un nouvel espace mémoire, L1 et L2 sont liée et les changement de L1 = changement sur L2
L3= copy.deepcopy(L1) #Ca copie mais les changement peuvent etre effectué sur L1 sans changement sur L3