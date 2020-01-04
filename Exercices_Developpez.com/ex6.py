#! /usr/bin/python
import os

nombre = int (input ("entrez un nombre : "))
compte = 0

i = nombre - 1
diviseur = []

while i > 1:
    if nombre % i == 0:
        diviseur.append(i)
        compte += 1

    i -= 1
if len(diviseur) == 0:
    print "aucun ! Il est premier"
else :
    print "Divisieur propres sans repetition de", nombre, ":",
    for x in range(len(diviseur)) :
        print diviseur[x],
    print "(soit", compte, "diviseur propres)"
