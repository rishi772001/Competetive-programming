'''
@Author: rishi
https://leetcode.com/problems/trapping-rain-water/
'''


# The water at any index is minimum of maxleft and maxright to that index
def trap(arr):
    ans = 0

    # store maxleft, maxright for all indices
    lmax = [arr[0]]
    rmax = [arr[-1]]

    for i in range(1, len(arr)):
        lmax.append(max(lmax[i - 1], arr[i]))

    for i in range(1, len(arr)):
        rmax.append(max(rmax[i - 1], arr[len(arr) - 1 - i]))

    # use maxleft and right to compute water level at that point
    for i in range(len(arr)):
        ans += min(lmax[i], rmax[-(i + 1)]) - arr[i]
    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
