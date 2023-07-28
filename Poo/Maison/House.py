"""
Créez une classe « House », avec un attribut « surface », un constructeur qui définit sa valeur et une 
méthode « Display » pour afficher « Je suis une maison, ma surface est de XXX m2 » (XXX: la valeur de 
surface). Incluez aussi des getters et des setters pour la surface.

La classe « House » contiendra une porte (Door). Chaque porte aura un attribut « color » (de type 
String), et une méthode « Display » qui affichera « Je suis une porte, ma couleur est bleu » (ou quelle 
que soit la couleur). Inclure un getter et un setter. Créez également la méthode « GetDoor » dans la 
classe « House ».

La classe « Apartment » est une sous-classe de la classe « House », avec une surface prédéfinie de 
50m2.
Créez également une classe Person, avec un nom (de type String). Chaque personne aura une maison. 
La méthode « Display » pour une personne affichera son nom, les données de sa maison et les 
données de la porte de cette maison.
Écrivez un Main pour créer un Apartment, une personne pour y vivre et pour afficher les données de 
la personne
"""

class House:
    __porte = "Bleue"
    
    def __init__(self, surface):
        self.set_surface(surface)
        
    
    def set_surface(self, valeur):
        self.__surface = valeur
    
    def get_surface(self):
        return self.__surface
    
    def Surface(self)->str:
        return print("Je suis une maison, ma surface est de ", self.get_surface()," m2")
    
    def CreatePorte(self, Couleur):
        self.__porte = Couleur
    
    def Get_Porte(self):
        return self.__porte
        
    def Display(self):
        return(print("Je suis une porte de couleur ", self.Get_Porte()))