# Find the number of paths between the start point and the final point using dynamic programming
# up, right and diagonal moves are allowed
# Suppose that N (1,1) = 0
# N (2, 2) = 3 otherwise it won't work


import os
x, y = 3, 5

matrix = [[0 for i in range (y+1)] for j in range (x+1)]

def NoP (n, m) :
    global matrix
    if matrix[n][m] != 0 :
        return matrix[n][m]
    if m == 1 and n == 1 :
        return 0
    if (m == 1 or n == 1) :
        return 1

    matrix[n][m] = NoP (n-1, m) + NoP (n, m-1) + NoP (n - 1, m - 1)
    return matrix [n][m]

if __name__ == "__main__" :
  matrix[2][2] = 3
  res = NoP (x, y)
  print res
