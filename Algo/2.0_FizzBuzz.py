# -*- coding: utf-8 -*-
"""
FizzBuzz !

But de l'exercice :

Afficher en console les nombres de 1 à 35 (un par ligne) en remplaçant les
multiples de 3 par "Fizz!" et les multiples de 5 par "Buzz!". Les
multiples de 3 et 5 seront remplacés par "FizzBuzz!".

"""
for i in range(1,36):
    if(i%3==0 and i%5==0):
        print("FizzBuzz!")
    if(i%3==0):
        print("Fizz!")
    if(i%5==0):
        print("Buzz!")
    else:
        print(i)
