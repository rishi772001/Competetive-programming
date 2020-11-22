# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(a):
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(cols):
            if (a[i][j] == 0):
                for k in range(j + 1, cols):
                    if(a[i][k] != 0):
                        a[i][k] = -99
                for k in range(i + 1, rows):
                    if a[k][j] != 0:
                        a[k][j] = -99

                for k in range(0, j):
                    if a[i][k] != 0:
                        a[i][k] = -99
                for k in range(0, i):
                    if a[k][j] != 0:
                        a[k][j] = -99


    for i in range(rows):
        for j in range(cols):
            if (a[i][j] == -99):
                a[i][j] = 0
print(setZeroes([[0,1,2,0],
           [3,4,5,2],
           [1,3,1,5]]))