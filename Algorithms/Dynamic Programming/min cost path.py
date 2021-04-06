# https://www.geeksforgeeks.org/min-cost-path-dp-6/

import sys

def min_cost_path_in_dp(cost):
    m = len(cost)
    n = len(cost[0])

    arr = [[0 for i in range(n)] for i in range(m)]


    arr[0][0] = cost[0][0]

    for i in range(1,m):
        arr[i][0] = arr[i-1][0] + cost[i][0]

    for i in range(1,n):
        arr[0][i] = arr[0][i-1] + cost[0][i]


    for i in range(1,m):
        for j in range(1,n):
            arr[i][j] = min(arr[i][j - 1], arr[i - 1][j]) + cost[i][j]

    for i in arr:
        print(i)

    print(arr[m - 1][n - 1])

# Bottom up approach
def min_cost_path_in_recursion(cost, i, j):
    """
    :param cost: 2d matrix
    :param i: last index to reach
    :param j: last index to reach
    :return: min sum
    """
    if i == 0 and j == 0:
        return cost[i][j]

    elif i < 0 or j < 0:
        return sys.maxsize

    else:
        return cost[i][j] + min(
            min_cost_path_in_recursion(cost, i - 1, j),
            min_cost_path_in_recursion(cost, i, j - 1),
        )


cost= [
  [1,3],
  [1,5]
]
min_cost_path_in_dp(cost)
print(min_cost_path_in_recursion(cost, len(cost) - 1, len(cost[0])))
