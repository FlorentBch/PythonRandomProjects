"""
Donner un algorithme qui détermine le prix d'entré dans un cinéma. (Les mineurs payent 5 euros, les autres
10 euros).

"""
Age = int(input("Quel est votre age ?"))

if(Age<18):
    print("Le prix de votre place est de 5euros au tarif mineur")
else:
    print("Le prix de votre place est de 10euros au tarif majeur")