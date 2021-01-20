'''
@Author: rishi
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

import sys


def largestsum(arr):
    # meh -> max sum ending here
    # msf -> max sum so far
    meh = 0
    # For arrays containing negative values
    msf = -sys.maxsize
    currstart = start = end = 0
    for i in range(len(arr)):
        # update max ending here
        meh = meh + arr[i]
        # if updated meh is less than this current element set meh to this
        if meh < arr[i]:
            currstart = i
            meh = arr[i]

        # update max so far if it is less than meh
        if msf < meh:
            # change main start, end if its msf is updated else discard
            start = currstart
            end = i
            msf = meh
    print(start, end)
    return msf


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largestsum(a))
