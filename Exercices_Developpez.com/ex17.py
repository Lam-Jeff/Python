#! /usr/bin/python
import os


def UniqueValue ( table ) :
    check_list = []
    i = 0
    while i < 500 :
        check_list.append (0)
        i += 1

    for value in range (len(table)) :
        if check_list [table[value]] == 0 :
            check_list [table[value]] = 1
        else :
            return False
    return True

if __name__ == "__main__" :
    table = [1, 5, 8, 9, 10 , 222, 5, 8]

    if UniqueValue (table) :
        print "pas de doublons !"
    else :
        print "valeurs non unique."
