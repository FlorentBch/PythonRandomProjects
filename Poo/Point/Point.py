"""
Créez une classe appelée « Point ». Cette classe doit avoir 2 entiers (x, y) en tant que membres privés. 
Le constructeur doit définir les valeurs de x et y via des paramètres. La classe doit avoir une méthode 
publique appelée « distance ». Cela prend un seul paramètre(Point) et renvoie la distance entre les 2 
points
"""
class Point:
    def __init__(self,x:int(),y:int()):
        self.set_x(x)
        self.set_y(y)
    
    def get_x(self):
        return(self.__x)
    
    def set_x(self, valeur):
        if(type(valeur)==int):
            self.__x = valeur
        else:
            raise TypeError("Veuillez entrer un type int svp")
    
    def get_y(self):
        return(self.__y)
    
    def set_y(self, valeur):
        if(type(valeur)==int):
            self.__y = valeur
        else:
            raise TypeError("Veuillez entrer un type int svp")
        
    def distance(self,Point):
        Point = self.get_x() - self.get_y()
        return Point