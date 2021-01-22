'''
@Author: rishi
https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
'''
import sys

"""
If differences between prefix sums of two arrays become same at two points, 
then subarrays between these two points have same sum.
"""

arr1 = [0, 1, 0, 0, 0, 0]
arr2 = [1, 0, 1, 0, 0, 1]


# ans = 6


def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]


prefix_sum(arr2)
prefix_sum(arr1)

d = {}
maxi = -sys.maxsize

for i in range(len(arr1)):
    val = arr1[i] - arr2[i]
    if val in d:
        maxi = max(maxi, i - d[val])
    else:
        d[val] = i
print(maxi)
