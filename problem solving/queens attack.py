#!/bin/python3

import math
import os
import random
import re
import sys
def valid(ob,r,c):
    if([r,c] in ob):
        return True
    else:
        return False
# Complete the queensAttack function below.
def queensAttack(n, k, r, c, ob):
    ans = 0
    # - in row
    for i in range(r - 1, 0, -1):
        if (valid(ob, i, c)):
            break
        else:
            ans += 1
    # - in col
    for i in range(c - 1, 0, -1):
        if (valid(ob,r, i)):
            break
        else:
            ans += 1
    # - in dia
    i = r - 1;
    j = c - 1
    while (i > 0 and j > 0):
        if (valid(ob, i, j)):
            break
        else:
            ans += 1
        i -= 1;
        j -= 1
    # +1 in row
    for i in range(r + 1, n+1):
        if (valid(ob,i, c)):
            break
        else:
            ans += 1
    # +1 in col
    for i in range(c + 1, n+1):
        if (valid(ob,r, i)):
            break
        else:
            ans += 1
    # +1 in dia
    i = r + 1
    j = c + 1
    while (i < n+1 and j < n+1):
        if (valid(ob,i,  j)):
            break
        else:
            ans += 1
        i += 1;
        j += 1
    # in another dia
    i = r - 1
    j = c + 1
    while (i > 0 and j < n+1):
        if (valid(ob, i,  j)):
            break
        else:
            ans += 1
        i -= 1
        j += 1
    # in another dia
    i = r + 1
    j = c - 1
    while (i < n+1 and j > 0):
        if (valid(ob, i,  j)):
            break
        else:
            ans += 1
        i += 1
        j -= 1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
