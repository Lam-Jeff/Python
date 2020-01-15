#'! /usr/bin/python
import os

# ex19 with 3 dices

def combination (n) :
    dice = [i+1 for i in range (6)]
    res = 0

    for i in range (len (dice)) :
        for j in range (len(dice)) :
            for k in range (len (dice)):
                if dice [i] + dice [j] + dice [k] == n :
                    res += 1
    return res


if __name__ == "__main__" :
    n = input ("entrez un nombre entre 3 et 18 : ")

    while n < 3 or n > 18 :
        n = input ("entrez un nombre e,tre 3 et 18 :")

    print combination (n)


