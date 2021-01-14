'''
@Author: rishi
https://binarysearch.com/problems/Integer-to-Base-3
'''


def solve(n, base):
    ans = ""
    negative = False
    # Check for negative
    if n < 0:
        negative = True
        # If yes, then change to positive
        n = n * -1

    while n > 0:
        ans += str(n % base)
        n = n // base

    if negative:
        return "-" + ans[::-1]
    return ans[::-1]
