"""

Premier :

Creer un script qui permet de definir 
si un nombre est premier ou non.

Si il ne l'est pas, le script doit me permetre 
de savoir
combien de fois il peut se diviser.

rappel : un nombre premier n'est divisible 
que par 1 et par lui meme!
"""


n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

i = 2 # plus petit diviseur possible de n
cpt = 0 # initialise le compteur de divisions
p = n/2 # calculé une fois dans la boucle

print("Diviseurs propres sans répétition de", n, " :", end=' ')
while i <= p :
    # si division complete, reste 0
    if n%i == 0:
        cpt += 1
        print(i, end=' ')
    i += 1

if not cpt :
    print("aucun ! Il est premier.")
else :
    print("(soit", cpt, "diviseurs propres)")