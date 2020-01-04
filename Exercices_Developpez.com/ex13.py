#! /usr/bin/python
import os
import random

def listAleaFloat (n) :
    liste = []

    i = 0
    while i < n :
        liste.append(random.random())
        i += 1
    return liste

if __name__ == "__main__" :
    nombre = input ("entrez un nombre entre 2 et 100 : ")

    liste = listAleaFloat (nombre)
    amplitude = max(liste) - min (liste)
    somme = sum (liste)
    moyenne = somme / float (len (liste))

    print liste
    print "amplitude de la liste : ", amplitude
    print "moyenne de la liste : ", moyenne

