'''
@Author: rishi
https://binarysearch.com/problems/K-Unique-String
'''


def solve(self, s, k):
    d = {}
    count = 0
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    if len(d) <= k:
        return count
    keys = sorted(d, key=d.get)

    to_delete = len(d) - k
    for i in range(to_delete):
        count += d[keys[i]]
    return count
