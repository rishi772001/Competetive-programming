'''
@Author: rishi
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''


def knapsack(totweight, wt, val, n):
    """
    :param totweight: total weight of knapsack
    :param wt: weight array of items
    :param val: values array of items
    :param n: number of items or len of wt or val
    """
    dp = [[0 for x in range(totweight + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(totweight + 1):
            # if this item can be added
            if wt[i - 1] <= w:
                # find max of this item added and not added
                # if added we need to check for that weight(curr wt - the wt of added item)
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[-1][-1]


items = [1, 2, 3]
values = [2, 5, 3]
totwt = 4
print(knapsack(totwt, items, values, len(items)))
