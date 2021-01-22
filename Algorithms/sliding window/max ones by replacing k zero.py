'''
@Author: rishi
https://www.techiedelight.com/find-maximum-sequence-of-continuous-1s-can-formed-replacing-k-zeroes-ones/
'''

import sys

arr = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]

start = end = count = 0

maxi = -sys.maxsize
k = 0

while end < len(arr):
    if arr[end] == 0:
        count += 1
    end += 1
    if count > k:
        count -= 1
        if end - start > maxi:
            maxi = end - start - 1
        while arr[start]:
            start += 1
        start += 1

if end - start > maxi:
    maxi = end - start
print(maxi)
