'''
@Author: rishi
https://leetcode.com/problems/climbing-stairs/
'''


def solve(n, memo={}):
    # Base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Check for already computed value
    if n in memo:
        return memo[n]
    # Recurrence relation
    val = solve(n - 1, memo) + solve(n - 2, memo)
    # Memoization
    memo[n] = val
    return val


print(solve(3))
