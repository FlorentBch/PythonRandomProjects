"""
Donner un algorithme qui détermine le prix d'entré dans un cinéma. (Les mineurs payent 5 euros, les autres
10 euros) avec un Dictionnaire de données

"""
#DictionnairePrix = {}
#DictionnairePrix["mineur"] = 5
#DictionnairePrix["majeur"] = 10
DictionnairePrix = {"mineur":5,"majeur":10 }
BoolAge = str(input("êtes vous mineur ou majeur ?"))

print("Le prix de votre place en tant que", BoolAge,"est au prix de ", DictionnairePrix.get(BoolAge), "€")
