#! /usr/bin/python
import os

#function de test de saisie
def valide (chaine) :
    if type (chaine) != str :
        return False
    chaine = chaine.upper()
    for char in chaine :
        if char not in "ATCG" :
            return False
    return True

#saisie function
def saisie () :
    chaine = raw_input()
    while not (valide (chaine)) :
        print "mauvaise saisie, recommencez"
        chaine = raw_input()
    return chaine

def proportion (chaine, sequence) :
    count = chaine.count(sequence)
    print count
    print "il y a ", count / float(len (chaine)) * 100.00, "% de", sequence, "dans la chaine"


if __name__ == "__main__" :
    print "entrez  une chaine de nucleotides : "
    chaine = saisie()
    print "entrez une sequence a trouver :"
    seq = saisie ()
    print "chaine : ", chaine
    print "sequence : ", seq
    proportion (chaine, seq)
