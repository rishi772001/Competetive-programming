'''
@Author: rishi
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    window = set()
    start = end = maxi = size = 0

    while end < len(s):
        if s[end] not in window:
            window.add(s[end])
            size += 1
            end += 1
        else:
            maxi = max(size, maxi)
            window.remove(s[start])
            start += 1
            size -= 1

    return max(maxi, size)
