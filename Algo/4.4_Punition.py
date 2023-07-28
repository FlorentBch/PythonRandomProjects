"""
Ecrire de 2 façon différentes le programme qui permet de faire la punition suivante :

Ecrire 100 fois :
    Je doit apprendre python pour progresser.
"""

cpt = 1
while cpt<101:
    print(cpt,".Je dois apprendre python pour progresser.")
    cpt+=1
    
for x in range(1,101,1):
    print(x,".Je dois apprendre python pour progresser.")