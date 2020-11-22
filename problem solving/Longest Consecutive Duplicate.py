'''
@Author: rishi
'''


def solve(s):
    max_val = 0
    curr = ""
    for i in range(len(s)):
        if curr == "" or s[i] == curr[0]:
            curr += s[i]
        else:
            l = len(curr)
            if l > max_val:
                max_val = l
            curr = "" + s[i]
    l = len(curr)
    if l > max_val:
        max_val = l

    return max_val


print(solve("aaabbbb"))