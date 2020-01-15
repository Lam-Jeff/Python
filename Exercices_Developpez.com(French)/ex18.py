#! /usr/bin/python
import os
from random import *

def CreateTable (n , a, b) :
    return [randint (a, b) for i in range (n)]

if __name__ == "__main__" :
    n = input ("Entrez un nombre entre 2 et 100 :")
    while n > 100 or n < 2 :
        n = input ("Entrez un nombre entre 2 et 100 :")
    seed ()
    init = CreateTable (n, 0, 500)
    test = list (set (init))

    if len (init) == len (test) :
        print ("Les elements sont distincts")
    else :
        print ("un element est repete")
    print init

