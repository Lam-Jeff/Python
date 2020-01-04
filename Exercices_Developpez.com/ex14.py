#! /usr/bin/python
import os
import random


def minMaxMoy (liste) :
    return (min (liste), max (liste), sum (liste) / float (len (liste)))


if __name__ == "__main__" :
    liste = [10, 18, 14, 20, 12, 16]

    mini, maxi, moy = minMaxMoy (liste)
    print mini, maxi, moy

