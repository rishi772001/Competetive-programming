'''
@Author: rishi
https://binarysearch.com/problems/Run-Length-Encoding
'''


def solve(s):
    curr = ""
    curr_len = 0
    ans = ""
    for i in range(len(s)):
        if curr == "":
            curr = s[i]
            curr_len += 1
        elif curr == s[i]:
            curr_len += 1
        else:
            ans += str(curr_len) + s[i - 1]
            curr = s[i]
            curr_len = 1
    ans += str(curr_len) + s[i]
    return ans
print(solve("AAAABBBCCDAA"))