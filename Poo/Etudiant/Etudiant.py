"""
Écrivez une classe appelée « Student » avec les membres suivant :
    •nom (de type String),
    •note1, note2 (de type int)
Le programme demande à l’utilisateur d’entrer le nom et les notes. calc_moy() calcule la note 
moyenne et show() affiche le nom et la note moyenne
"""


class Etudiant:
    def __init__(self, nom: str = "Null", note1: int = 0, note2: int = 0):
        self.set_nom(nom)
        self.set_note1(note1)
        self.set_note2(note2)

    def get_nom(self):
        return (self.__nom)

    def set_nom(self, valeur):
        if (type(valeur) == str):
            self.__nom = valeur
        else:
            raise TypeError("Veuillez entrer un type String svp")

    def get_note1(self):
        return (self.__note1)

    def set_note1(self, valeur):
        if (type(valeur) == int):
            self.__note1 = valeur
        else:
            raise TypeError("Veuillez entrer un type int svp")

    def get_note2(self):
        return (self.__note2)

    def set_note2(self, valeur):
        if (type(valeur) == int):
            self.__note2 = valeur
        else:
            raise TypeError("Veuillez entrer un type int svp")

    def inputUser(self):
        nom = str(input("Entrez votre nom"))
        note1 = int(input("Entrez votre note 1"))
        note2 = int(input("Entrez votre note 2"))

        self.set_nom(nom)
        self.set_note1(note1)
        self.set_note2(note2)

    def calc_moy(self):
        return ((self.get_note1()+self.get_note2())/2)

    def show(self):
        message = print(self.get_nom(), ": ", self.calc_moy())
        return (message)
