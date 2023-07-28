"""
Écrivez une classe « Rectangle » ayant deux variables « a » et « b » et une fonction membre 
« surface() » qui retournera la surface du rectangle.

"""
'''
    classe Rectangle permettant de calculer la surface de l'objet
'''

class Rectangle:
    '''
        Définir deux attributs (a et b) en passant par le setter getter
        Définir une méthode permettant de calculer la surface du rectangle
        Définir une méthode permettant l'affichage de cette surface
    '''

    def __init__(self, a, b):
        self.setLargeur(a)  # appel du setter pour largeur
        self.longueur = b   # appel du setter pour longueur

    # nous définissons les getters setters pour nos attributs
    # (ils permettent de les créer et de mettre des contraintes à leurs valeurs)
    @property
    def longueur(self):
        '''
        getter de longueur
        :return: la longueur
        '''
        return self.__longueur

    @longueur.setter
    def longueur(self, valeur):
        '''
        setter de longueur
        :param valeur: int ou float
        :return: none
        '''
        if type(valeur) == int or type(valeur) == float : # si la valeur est un nombre nous l'affectons à la variable
            self.__longueur = valeur
        else :  # sinon nous levons une exception
            raise TypeError("Veuillez renseigner des nombres pour la longueur")

    def getLargeur(self):
        '''
        getter de largeur
        :return: float ou int
        '''
        return self.__largeur

    def setLargeur(self, valeur):
        '''
        setter de largeur
        :param valeur: int ou float
        :return: none
        '''
        if type(valeur) == int or type(valeur) == float : # si la valeur est un nombre nous l'affectons à la variable
            self.__largeur = valeur
        else :  # sinon nous levons une exception
            raise TypeError("Veuillez renseigner des nombres pour la largeur")

    def surface(self):
        '''
        méthode permettant la multiplication de 2 valeurs
        :return: float
        '''
        return self.__largeur * self.__longueur

    def __str__(self):
        '''
            transforme un objet en chaine de caractère
            retourne la longueur, la largeur et la surface de notre rectangle
        :return: str
        '''
        return f"longueur : {self.__longueur} \n largeur : {self.__largeur} \n surface : {self.surface()}"