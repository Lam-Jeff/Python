import os

# Recursive for dice problem
# formula is : N(d, s) = N(d, s - 1) + N(d - 1, s - 1) - N(d - 1, s - 7)


def combination (nbd, s) :
    if nbd == s :
        return 1
    elif nbd == 0 or s < nbd :
        return 0
    else :
        return combination (nbd, s - 1) + combination (nbd - 1, s - 1) - combination (nbd - 1, s - 7)


if __name__ == "__main__" :
    dices = input ("enter number of dices : ")
    number = input ("enter number you want to get : ")

    print combination (dices, number)

