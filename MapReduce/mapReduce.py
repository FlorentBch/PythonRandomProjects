from collections import defaultdict

def wordCount(text):

    '''
    fonction qui sert à compter les mots d'un texte
    @param : du texte
    @return : dictionnaire [clé: mot, valeur: son occurence]
    '''
    counts=defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts

# ======================================
# modification en mapreduce de ce programme simple
# ======================================

def map(key, value):
    """Fonction qui permet de transformer l'element clé/ valeur en liste d'element mot, occurence

    Args:
        key (_type_): _description_
        value (_type_): _description_
    """
    intermediaire=[]
    for word in value.split():
        intermediaire.append((word.lower(),1))
    return intermediaire

def reduce(key, values):
    """Fonction qui permet de fusionner les occurences de la liste des valeurs en une seule valeur

    Args:
        key (_type_): _description_
        values (_type_): _description_

    Returns:
        _type_: _description_
    """
    value = 0
    for chaque_element in values:
        value += chaque_element
    return (key, value)