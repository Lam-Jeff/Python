#! /usr/bin/python
import os

def RomanNumber (n) :
    number = [1, 4, 5, 9, 10, 40,  50, 90, 100, 400, 500, 900, 1000]
    letter = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    table = zip (number, letter)


    for d, r in sorted (table, reverse = True):
        while d <= n :
            print r,
            n = n - d


if __name__ == "__main__" :
    number = input ('enter a number between 1 and 4000 : ')
    RomanNumber (number)
