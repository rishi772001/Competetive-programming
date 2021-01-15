'''
@Author: rishi
https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/
next steps 1st point
'''

from collections import defaultdict


def solve(initspeed, path, memo, steps, startingindex=0):
    """
    :param initspeed: starting speed
    :param path: boolean array representing 1 as spikes
    """

    # check for already computed value
    steps.append(startingindex)

    if startingindex in memo and initspeed in memo[startingindex]:
        if memo[startingindex][initspeed]:
            return True
        steps.pop()
        return False

    # Base case
    if 0 > startingindex or startingindex >= len(path):
        # memoization
        steps.pop()
        memo[startingindex][initspeed] = False
        return False

    elif path[startingindex] == 1:
        # memoization
        steps.pop()
        memo[startingindex][initspeed] = False
        return False
    if initspeed == 0:
        # memoization
        memo[startingindex][initspeed] = True
        return True

    # recurrence relation
    if (solve(initspeed - 1, path, memo, steps, startingindex + initspeed - 1) or
            solve(initspeed + 1, path, memo, steps, startingindex + initspeed + 1) or
            solve(initspeed, path, memo, steps, startingindex + initspeed)):
        return True
    steps.pop()
    return False


path = [0, 1, 0, 1, 0, 0]
memo = defaultdict(dict)
steps = []
print(solve(2, path, memo, steps=steps))
print(steps)
