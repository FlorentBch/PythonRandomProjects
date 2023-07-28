from Person import Person
"""
    La classe « Student » aura une méthode publique « DisplayAge » qui écrira sur l’écran « My age is: 
XX years old 

"""

class Student(Person) :
    def __init__(self):
        pass
    
    def GoToClasses(self):
        return(print("Im going to class !"))
    
    def DisplayAge(self):
        print(super().get_age())