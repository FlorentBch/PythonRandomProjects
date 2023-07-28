'''
    fichier permettant l'instance de la classe Rectangle
'''

from Rectangle import Rectangle

try :
    rectangle = Rectangle(5,10)
    print(rectangle)
except TypeError as e:
    print(e)