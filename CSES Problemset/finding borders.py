'''
@Author: rishi
https://cses.fi/problemset/task/1732
'''

s = input()

prefixes, suffixes = set(), set()

prefix, suffix = "", ""

for i in range(len(s) - 1):
    prefix += s[i]
    suffix = s[len(s) - 1 - i] + suffix
    prefixes.add(prefix)
    suffixes.add(suffix)

ans = prefixes.intersection(suffixes)
for i in ans:
    print(len(i), end=" ")
