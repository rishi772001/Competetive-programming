'''
@Author: rishi
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
'''
import sys

s = "BBBB"

window = {}
start = end = 0
maxi = -sys.maxsize
ans = []

while end < len(s):
    if s[end] in window:
        val = window[s[end]]

        if end - start > maxi:
            maxi = end - start
            ans = [start, end]
        while start <= val:
            start += 1

    window[s[end]] = end
    end += 1

if end - start > maxi:
    maxi = end - start
    ans = [start, end]

print(maxi)
print(s[ans[0]: ans[1]])
