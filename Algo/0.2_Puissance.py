"""
Puissance 2 

Ecrire un script qui determine le nombre de fois qu'un nombre est divisible par 2
"""

Nombre = int(input("Inidiquez votre nombre"))

cpt=0
ModuloNombre =Nombre
while(ModuloNombre%2==0):
    cpt+=1
    ModuloNombre//=2

print(str(Nombre)+" est divisible "+ str(cpt)+" fois par 2")
