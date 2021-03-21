'''
@Author: rishi
https://binarysearch.com/problems/Find-the-Largest-Number-in-a-Rotated-List
'''


def binarysearch(arr, l, r):
    # This condition is for the case when array is not rotated at all
    if arr[r] > arr[l]:
        return 0

    # If there is only one element left
    if l == r:
        return l

    while l <= r:
        mid = l + (r - l) // 2
        if mid < r and arr[mid + 1] < arr[mid]:
            return mid

        if mid > l and arr[mid] < arr[mid - 1]:
            return mid - 1

        # not sorted -> so it contains the max
        if arr[l] > arr[mid]:
            r = mid - 1
        # other half contains the max
        else:
            l = mid + 1


def solve(arr):
    ind = binarysearch(arr, 0, len(arr) - 1)
    return arr[ind]


print(solve([3, 4, 5, 1, 2]))
