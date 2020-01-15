#! /usr/bin/python
import os
import random

def listAleaInt (n, a, b) :
    liste = []

    i = 0
    while i < n :
        liste.append(random.randint(a, b))
        i += 1
    return liste

def switch (liste) :
    minimum = min (liste)
    position = liste.index (minimum)
    tmp = liste[0]
    liste[0] = liste[position]
    liste[position] = tmp


if __name__ == "__main__" :
    n = input ("nombre d'elem ? : ")
    liste = listAleaInt (n, 10, 50)
    print liste
    switch(liste)
    print liste

