'''
@Author: rishi
https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
'''


def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]


arr = [-7, 1, 5, 2, -4, 3, 0]
prefix_sum(arr)
for i in range(len(arr)):
    if arr[i - 1] == arr[-1] - arr[i]:
        print(i)
        exit(0)
print("-1")
