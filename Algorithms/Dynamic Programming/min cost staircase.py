'''
@Author: rishi
'''


# Bottom up approach
def solve(cost):
    for i in range(2, len(cost)):
        cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])


cost = [10, 15, 20]
print(solve(cost))
