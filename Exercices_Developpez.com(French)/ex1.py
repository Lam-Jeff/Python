#! /usr/bin/python
from math import *
import os

def main ():
    hauteur = input ("entrez une hauteur : ")
    rayon = input ("entrez un rayon : ")
    print ("calcul du volume d'un cone...")
    volume = hauteur * rayon * rayon * pi / 3
    print "le volume : ", volume


if __name__ == "__main__" :
    main()
