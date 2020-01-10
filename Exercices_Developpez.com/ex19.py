#! /usr/bin/python

import os

# give number of combination possible for n given 2 dices
def combination (n) :
    de1 = [i+1 for i in range (6)]
    de2 = [i+1 for i in range (6)]

    res = 0
    for i in range (len (de1)) :
        for j in range (len (de2)) :
            if i + j == n :
                res += 1
    return res


if __name__ == "__main__" :
    n = input ("Entrez un nombre entre 2 et 12 : ")
    while n < 2 or  n > 12 :
        n = input ("Entrez une valeur entre 2 et 12 :")

value = combination (n)
print value
