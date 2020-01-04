#! /usr/bin/python
import os


def RomanNumber (n) :
    values = {

        1000 : 'M',
        900 : 'CM',
        500 : 'D',
        400 : 'CD',
        100 : 'C',
        90 : 'XC',
        50 : 'L',
        40 : 'XL',
        10 : 'X',
        9 : 'IX',
        5 : 'V',
        4 : 'IV',
        1 : 'I'
    }

    for key in sorted (values, reverse = True) :
        while key <= n :
            print values [key],
            n = n - key



if __name__ == "__main__" :
    number = input ("enter a value between 1 and 3999 : ")
    RomanNumber (number)
