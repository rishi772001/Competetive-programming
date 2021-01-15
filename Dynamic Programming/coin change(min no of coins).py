'''
@Author: rishi
https://leetcode.com/problems/coin-change/
'''

mini = 2 ** 32


def solve(coins, amount, sum=0):
    global mini
    # Base Case
    if amount == 0:
        mini = min(mini, sum)
        return
    elif amount < 0 or coins == []:
        return
    # Memoization
    # Recurrence relation
    solve(coins, amount - coins[-1], sum + 1)
    solve(coins[:-1], amount, sum)


coins = [2]
amount = 3
solve(coins, amount)
print(mini) if mini < 2 ** 32 else print("-1")
