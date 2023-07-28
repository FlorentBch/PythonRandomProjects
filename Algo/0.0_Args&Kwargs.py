# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

#####
#Différence entre parametre de base et un *args
#####


# sum_integers_args.py
def my_sum(*args):  #args peut etre remplacé par un nom de variable basique, c'est l'étoile qui compte
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))


my_lambda = lambda *args : sum(args)
print(my_lambda(1,2,3))

####################################################################
##**Kwargs


# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))