"""

    écrire l'algorithme permettant de compter
    le nombre d'occurence des mots dans
    un fichier

"""
mot = input("Saisir le mot à chercher : ")

def WordOccurence(mot):
    with open("C:/Users/Administrateur/Documents/Pythonmots.txt", "r") as fichier:
        count = 0
        #print(fichier.read())
        mots = fichier.read().split(' ')
        for k in range(0, len(mots)):
            if mot == mots[k].lower() or mot+"," == mots[k].lower() or mot+"?" == mots[k] or mot+"!" == mots[k].lower() or mot+"." == mots[k].lower():
                print(mots[k])
                count += 1
        
        if count > 0:
            print(f"Le mot '{mot}' apparait {count} fois.")
        else:
            print(f"Le mot '{mot}' n'apparait pas.")

WordOccurence(mot)