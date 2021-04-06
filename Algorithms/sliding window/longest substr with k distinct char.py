'''
@Author: rishi
https://www.techiedelight.com/find-longest-substring-containing-k-distinct-characters/
'''
import sys

s = "aabacbebebe"
k = 3
# cbebebe - 7 -> output

window = {}
start = end = 0
ans = []

maxi = -sys.maxsize
while end < len(s):
    if s[end] in window:
        window[s[end]] += 1
    else:
        window[s[end]] = 1
    while len(window) > k:
        if window[s[start]] == 1:
            window.pop(s[start])
        else:
            window[s[start]] -= 1
        start += 1
    if len(window) == k:
        val = end - start + 1
        if val >= maxi:
            maxi = val
            ans = [start, end + 1]

    end += 1

if len(window) == k:
    val = end - start
    if val > maxi:
        maxi = val
        ans = [start, end]
print(maxi)
print(ans)
print(s[ans[0]: ans[1]])
