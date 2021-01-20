'''
@Author: rishi
https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
ref vdo -> https://www.youtube.com/watch?v=zQrR8t7urEE
'''
import sys


def mcm(arr, l, r):
    if l >= r:
        return 0
    mini = sys.maxsize
    for i in range(l, r):
        mini = min(mini,
                   mcm(arr, l, i) +
                   mcm(arr, i + 1, r) +
                   # no of operations = left mat[row] * left mat[col] * ri8 mat[col]
                   # the dividing point is i -> left matrix oda col value
                   arr[l - 1] * arr[i] * arr[r])
    return mini


print(mcm([1, 2, 3, 4], 1, 3))
