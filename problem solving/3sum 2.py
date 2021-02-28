'''
@Author: rishi
'''


def two_sum(nums, k, l):
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == k:
            return True
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            l += 1
    return False


def solve(nums, k):
    if len(nums) < 3:
        return False
    nums.sort()
    for i in range(len(nums)):
        to_find = k - nums[i]
        if two_sum(nums, to_find, i):
            return True
    return False


print(solve([4, 1, 2, 3], 5))
