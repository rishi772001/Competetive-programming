'''
@Author: rishi
https://leetcode.com/problems/coin-change/
'''


def solve(coins, amount):
    ans = 0
    coins = sorted(coins, reverse=True)
    amt = amount

    for j in range(len(coins)):
        amount = amt
        ans = 0
        for i in range(j, len(coins)):
            if coins[i] <= amount and coins[i] != 0:
                a = amount // coins[i]
                amount -= coins[i] * a
                ans += a

        if amount == 0:
            return ans
    return -1

denominations = [7, 62]
amount = 499
print(solve(denominations, amount))