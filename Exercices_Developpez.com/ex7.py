#! /usr/bin/python
import os

# def fac (n) :
#     if n == 1:
#         return 1
#     else :
#         return n * fac (n - 1)
#

def fac (n) :
    r = 1
    for x in range (r, r + 1) :
        r *= x
    return r

number = int (input ("valeur de n ? ; "))
exp = 0.0

for x in range(number) :
    exp = exp + 1.0 / fac (x)

print "approximation de l'exponentielle :", exp
