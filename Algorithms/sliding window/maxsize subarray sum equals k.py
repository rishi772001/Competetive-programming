'''
@Author: rishi
https://www.techiedelight.com/find-subarray-having-given-sum-given-array/
'''
import sys

a = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
s = 15

start = end = 0
window_sum = 0
ans = []
maxi = -sys.maxsize

while end < len(a):
    window_sum += a[end]
    while window_sum > s:
        window_sum -= a[start]
        start += 1
    if window_sum == s:
        if (end - start + 1) > maxi:
            maxi = end - start + 1
            ans = [start, end]
    end += 1

print(ans)
