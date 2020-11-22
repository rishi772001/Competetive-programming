'''
@Author: rishi
https://binarysearch.com/problems/Steady-Car
'''


def solve(a):
    ans = 0
    curr = None
    temp = 0
    for i in range(len(a) - 1):
        if curr is None:
            curr = abs(a[i] - a[i + 1])
            temp += 1

        elif abs(a[i] - a[i + 1]) == curr:
            temp += 1

        else:
            ans = max(ans, temp)
            curr = abs(a[i] - a[i + 1])
            temp = 1

    return max(ans, temp) + 1

print(solve([0, 3, 6, 5, 4, 3, 1, 7, 10, 13]))