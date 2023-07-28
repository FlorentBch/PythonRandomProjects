"""
Romain :

Ecrir un script qui permet de saisir un entier 
entre 1 et 3999
(pourquoi cette limitation ?).


Le script doit permettre de l'afficher en 
chiffre romain.

En bonus : le convertisseur inverse
"""


Nombre=0
while Nombre<1 or Nombre>3999:
    Nombre = int(input("Entrez un chiffre entre 1 et 3999"))
    
Chiffre = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}


def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:   #Tant que Number n'est pas egal à 0 on continue la boucle
        div = number // num[i]      #La division est égale au nombre rentré / par 1000 (soit le plus grand nombre possible)
        number %= num[i]            #On divise le nombre 
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
  
# Driver code
if __name__ == "__main__":
    number = Nombre
    print("Chiffre Romain:", end = " ")
    printRoman(number)