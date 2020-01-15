#! /usr/bin/python
import os


# TVA France decembre 2019
TVA = 1.200

flag = 1

while flag :
    HT = input ("entrez votre prix HT : ")
    print ("appuyez sur o pour confirmer votre choix : ")
    touche = raw_input()
    if touche == 'o' :
        flag = 0
    else :
        print ("vous n'avez pas appuye sur la touche o, recommencez...")


TTC = HT * TVA
print "le prix TTC est de : ", TTC
