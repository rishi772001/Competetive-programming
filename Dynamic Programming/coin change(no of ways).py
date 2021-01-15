'''
@Author: rishi
https://www.geeksforgeeks.org/coin-change-dp-7/
https://leetcode.com/problems/coin-change-2/
'''


def solve(coins, ans, amount, memo):
    m = len(coins) - 1

    # check for already computed value
    if memo[amount - 1][m] != -1:
        return memo[amount][m]

    # Base case
    if amount < 0 or coins == []:
        return 0
    if amount == 0:
        return 1

    # recurrence relation
    ans = ans + solve(coins[:-1], ans, amount, memo) + solve(coins, ans, amount - coins[-1], memo)

    # Memoization
    memo[amount - 1][m] = ans

    return ans


coins = [1, 2, 3]
amount = 4
memo = [[-1] * len(coins) for i in range(amount)]
print(solve(coins, 0, amount, memo))
