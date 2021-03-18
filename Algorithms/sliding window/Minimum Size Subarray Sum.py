'''
@Author: rishi
https://leetcode.com/problems/minimum-size-subarray-sum/
'''
import sys


def minSubArrayLen(target, arr):
    left, right = 0, 0
    curr_sum = 0
    ans = sys.maxsize
    while right < len(arr):
        curr_sum += arr[right]
        right += 1

        while curr_sum >= target:
            ans = min(ans, (right - left))
            curr_sum -= arr[left]
            left += 1

    if ans == sys.maxsize:
        return 0
    return ans
