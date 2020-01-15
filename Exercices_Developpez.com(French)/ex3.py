#! /usr/bin/python
import os


nombreGrand, nombreDonnees, resultat = 0, 0, 0

x = int (input ("entrez un nombre :( 0 ou moins stop ) "))

while x > 0 :
    resultat += x
    nombreDonnees += 1
    if x > 100 :
        nombreGrand += 1
    x -= 1

print "Somme : ", resultat
print "Nombres superieure a 100 : ", nombreGrand
print "Total de donnees : ", nombreDonnees
