#! /usr/bin/python
import os



def hauteurParcourue (numberStairs, height) :
    # 5 fois par jour
    heightM = height / 100.00
    distance = 35 * heightM * 2
    print "Pour", numberStairs, "marches de", height, "cm, il parcourt", distance,"m par semaine"


stairs = int (input ("number of stairs : "))
height = int (input ("stair's height :"))


hauteurParcourue (stairs, height)
