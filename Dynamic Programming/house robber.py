'''
@Author: rishi
https://leetcode.com/problems/house-robber/
'''
from collections import defaultdict


def solve(cost, memo, amount=0):
    # check for already computed value
    if len(cost) in memo and amount in memo[len(cost)]:
        return memo[len(cost)][amount]
    # Base Case
    if cost == []:
        return amount
    # Recurrence relation
    val = max(solve(cost[:-2], memo, amount + cost[-1]), solve(cost[:-1], memo, amount))
    # Memoization
    memo[len(cost)][amount] = val
    return val


cost = [1, 2, 3, 1]
memo = defaultdict(dict)
print(solve(cost, memo))
