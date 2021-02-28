'''
@Author: rishi
https://binarysearch.com/problems/Find-the-Largest-Number-in-a-Rotated-List
'''


def binarysearch(arr, l, r):
    if arr[r] > arr[l]:
        return 0

    if l == r:
        return l

    while l <= r:
        mid = l + (r - l) // 2
        if mid < r and arr[mid + 1] < arr[mid]:
            return mid

        if mid > l and arr[mid] < arr[mid - 1]:
            return mid - 1

        if arr[l] > arr[mid]:
            r = mid - 1
        else:
            l = mid + 1


def solve(arr):
    ind = binarysearch(arr, 0, len(arr) - 1)
    return arr[ind]


print(solve([5, 8, 3]))
