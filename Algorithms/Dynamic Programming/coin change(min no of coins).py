'''
@Author: rishi
https://leetcode.com/problems/coin-change/
'''

mini = 2 ** 32

"""
                                [1,2,5] 0
                    [1,2] 0                     [1,2,5] 5
            [1] 0       [1,2] 2             [1,2] 5                     [1,2,5] 10
        [] 0   [1] 1  [1] 2  [1, 2] 4     [1] 5   [1, 2] 7        [1, 2] 10     [1, 2, 5] 15
"""

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


coins = [1, 5, 2]
amount = 11
solve(coins, amount)
print(mini) if mini < 2 ** 32 else print("-1")
