'''
@Author: rishi
https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/
'''
from collections import defaultdict


def solve(initspeed, path, memo, startingindex=0):
    """
    :param initspeed: starting speed
    :param path: boolean array representing 1 as spikes
    """

    # check for already computed value
    if startingindex in memo and initspeed in memo[startingindex]:
        return memo[startingindex][initspeed]

    # Base case
    if 0 > startingindex or startingindex >= len(path):
        # memoization
        memo[startingindex][initspeed] = False
        return False

    elif path[startingindex] == 1:
        # memoization
        memo[startingindex][initspeed] = False
        return False
    if initspeed == 0:
        # memoization
        memo[startingindex][initspeed] = True
        return True

    # recurrence relation

    if (solve(initspeed - 1, path, memo, startingindex + initspeed - 1) or
            solve(initspeed + 1, path, memo, startingindex + initspeed + 1) or
            solve(initspeed, path, memo, startingindex + initspeed)):
        memo[startingindex][initspeed] = True
        return True
    return False


path = [0, 1, 0, 0]
memo = defaultdict(dict)
print(solve(2, path, memo))
print(memo)
