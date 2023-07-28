from Person import Person

class Teacher(Person):
    def __init__(self, subject):
        self.set_subject(subject)
    
    def set_subject(self, valeur):
        if(type(valeur)==str):
            self.__subject = valeur
        else:
            raise TypeError("Veuillez entrer un str")
    
    def get_subject(self):
        return self.__subject
    
    def Explain(self)->str:
        return (print("Explanation begins !"))