'''
@Author: rishi
https://leetcode.com/problems/find-pivot-index
'''


def pivotIndex(nums):
    if not nums:
        return -1

    a = [nums[0]]
    for i in range(1, len(nums)):
        a.append(nums[i] + a[i - 1])

    print(a)

    if a[-1] - a[0] == 0:
        return 0

    for i in range(1, len(nums)):
        if a[i - 1] == a[-1] - a[i]:
            return i
    return -1

print(pivotIndex([-1,-1,-1,-1,1,1]))