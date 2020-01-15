#! /usr/bin/python
import os


def amende (poule, chien, vache, ami) :
    pointPerdus = poule + 3 * chien + 5 + vache + 10 * ami
    nbrePermis = pointPerdus / 100.0
    return nbrePermis * 200


poule = int (input ("nombre de poules :"))
chien = int (input ("nombre de chiens :"))
vache = int (input ("nombre de vaches :"))
ami = int (input ("nombre de amis :"))

payer = amende (poule,chien, vache, ami)
if payer :
    print "somme a payer :", payer
else :
    print "rien a payer"


