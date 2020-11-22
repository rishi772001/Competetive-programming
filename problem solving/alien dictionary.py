'''
@Author: rishi
'''


def solve(d, s):
    if d == "":
        return True

    index = 0
    count = 0

    for i in d:
        if i in s:
            count += 1

    for i in range(len(s)):
        if s[i] != " " and s[i] in d and s[i] != d[index]:
            index += 1
        if index >= len(d) or index > count:
            return False

    return True


dictionary = "jugm"
s = "xuaccfikwwjyz"
print(solve(dictionary,s))