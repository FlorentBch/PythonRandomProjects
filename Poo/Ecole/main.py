"""
– Créez une classe « Person »
– Créez une classe « Student » et une autre classe « Teacher », les deux héritent de la classe « Person ».
– La classe « Student » aura une méthode publique « GoToClasses », qui affichera à l’écran « I’m going
to class. ».
– La classe « Teacher » aura une méthode publique « Explain », qui affichera à l’écran « Explanation
begins ». En plus, il aura un attribut privé « subject » de type string.
– La classe « Person » doit avoir une méthode « SetAge(int n) » qui indiquera la valeur de leur âge (par 
exemple, 15 years old).
– La classe « Student » aura une méthode publique « DisplayAge » qui écrira sur l’écran « My age is: 
XX years old ».

– Vous devez créer une autre classe de test appelée « Test » qui contiendra « Main » et:
– Créez un objet Person et faites-lui dire « Hello »
– Créer un objet Student, définir son âge à 15 ans, faites-lui dire « Hello », « I’m going to class. » et 
afficher son âge
– Créez un objet Teacher, 40 ans, demandez-lui de dire « Hello » puis commence l’explication
"""
from Student import Student, Person
from Teacher import Teacher

Personne = Person()
eleve = Student()
Prof = Teacher("Cours de Python")

Personne.Hello()
eleve.set_Age(15)
eleve.Hello()
eleve.GoToClasses()
eleve.DisplayAge()

Prof.set_Age(40)
Prof.Hello()
Prof.Explain()


