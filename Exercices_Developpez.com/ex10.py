#! /usr/bin/python
import os


def tchacatchac (vitesse) :
    heure = 9 + int (170 / vitesse)
    minute = int (60 * 170 / vitesse) % 60
    print "Mort a :", heure, "h:", minute, "m"



i = 100

while i <= 300 :
    tchacatchac (i)
    i += 10
