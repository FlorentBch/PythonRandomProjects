"""

ecrire l'algorithme qui inverse
l'ordre des mots d'une phrase

ecrire l'algorithme qui inverse
l'ordre des lettres d'une phrase

"ceci n'est pas un poulet "
"poulet un pas n'est ceci"
"teluop nu sap tse'n icec"

"""
phrase = input("Entrez votre phrase")

def InverseMots(phrase:str)-> str:
    tbl = phrase.split()
    for i in range (len(tbl)//2):
        tbl[i], tbl[len(tbl)-1-i] = tbl[len(tbl)-1-i], tbl[i]
    return(' '.join(tbl))

def InverseLettre(phrase:str)->str:
    tbl = []
    for l in phrase:
        tbl.append(l)
    
    for i in range (len(tbl)//2):
        tbl[i], tbl[len(tbl)-1-i] = tbl[len(tbl)-1-i], tbl[i]

    return(''.join(tbl))

print(InverseMots(phrase))
print(InverseLettre(phrase))