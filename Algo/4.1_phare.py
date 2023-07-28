"""
Phare :

Un gardien de phare doit se rendre au toillette 5 fois par jour.
Malheuresement, elle se trouve au rez-de-chaussé.

Creer un script qui permet calculer pour x marche de y cm
la distance parcourue par semaine de se gardien de phare.

astuce : une fois terminer il doit remonté

bonus : afficher une tour qui à la largeur des marches en *
et un nombre d'etage correspondant au nombre de marches

"""

NombreMarche = 0
MesureMarche = 0
DistanceParcourue = 0
AllerRetour = 5*2
cpt=0

def CalculDistance (Nombre, Mesure)->int:
    return (Nombre*Mesure)*10
def ConvertToKm(Metre)->float:
    return Metre/1000
def Semaine (Nombre)->int:
    return Nombre*7
def CalculParSemaine (NbMarche, NbMesure) ->float:
    return Semaine(ConvertToKm(CalculDistance(NbMarche,NbMesure)))

NombreMarche = int(input("Combien de marche contient le phare ?"))
MesureMarche = int(input("Très bien ! Maintenant combien de centimètre font les marches ?"))

DistanceParcourue = CalculDistance(NombreMarche,MesureMarche)
print("Cela représente ",CalculParSemaine(NombreMarche,MesureMarche),"en km et par semaine soit",DistanceParcourue," métres par jours")

# for i in range (NombreMarche):
#     for j in range (MesureMarche):
#         print(((MesureMarche-j)-1)*" ","*")
#         cpt+=1
#         if cpt==NombreMarche:
#             break

while cpt<NombreMarche:
    for j in range (MesureMarche):
        if(cpt>=NombreMarche):
            break
        print(((MesureMarche-j)-1)*" ","*")
        cpt+=1
