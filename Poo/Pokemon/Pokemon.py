"""
Contexte : 
Vous connaissez certainement tous ces petites bêtes toute mignonnes (ou pas pour certaines)
Ces petites créatures sont dressées par des "dresseurs de pokemons" et sont amenées à combattre entre elles.
Et bien, nous allons aussi les faire combattre !
Les Pokémon sont certes de très mignonnes créatures, mais ils sont également un bon exemple pour illustrer l’héritage. 

Je vous propose de commencer par créer une classe "Pokemon" qui contient les champs suivants : 
    ▪ un attribut nom qui représente le nom du Pokémon.
    ▪ un attribut hp (pour Health Points) qui représente les points de vie du Pokémon.
    ▪ un attribut qui s’appelle atk qui représente la force de base de l’attaque du Pokémon.
    ▪ un constructeur pour instancier des Pokémon adéquatement.
    ▪ une méthode isDead() qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.

Créez une méthode "attaquer(Pokemon p)" qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. 
L’attaque déduit atk points de la vie hp du Pokémon attaqué p.

Redéfinissez la méthode toString() qui va nous permettre d'afficher  les informations du Pokémon.

En plus des Pokémon dit "normaux" (décrits à travers la classe Pokemon), on ressence trois types de Pokémon :
    ▪ Les Pokémon de type Feu
    ▪ Les Pokémon de type Eau
    ▪ Les Pokémon de type Plante 
(en réalité il existe 17 types en tout mais on ne va pas s’amuser à tous les coder)

les Pokémon de type Feu sont super efficaces contre les Pokémon de type Plante et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Eau sont super efficaces contre les Pokémon de type Feu et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Plante et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Plante sont super efficaces contre les Pokémon de type Eau et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Plante ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

Créez trois classes : 
    ▪ PokemonFeu
    ▪ PokemonEau
    ▪ PokemonPlante
Ces classes héritent de la classe Pokemon et qui représentent les trois types de Pokémon 
susmentionnés. 
Ensuite, amusez-vous à faire des combats de Pokémon.
"""
from abc import ABC 
class Pokemon(ABC) :

    def __init__(self, hp, atk, name):
        self.atk = atk
        self.hp = hp
        self.name = name
        self.isDead = False
    
    def set_hp(self, valeur):
        self.hp = valeur
        
    def get_hp(self):
        return print("Les HP restant de votre Pokemon sont de",self.hp)
    
    def set_atk(self, valeur):
        self.atk = valeur
    
    def get_atk(self):
        return print("La valeur de votre attaque est de",self.atk)
        
    def set_name(self, valeur):
        self.name = valeur
    
    def get_name(self):
        return print("Votre Pokemon s'apelle",self.name )
    
    def isDead(self)->bool:
        if(self.hp<=0):
            self.__isDead = True
            "Votre Pokemon est mort !"
        else:
            self.__isDead = False
        return self.__isDead
    
    def attaquer(self, Poke):
        Poke.hp = Poke.hp - self.atk
        return Poke.hp