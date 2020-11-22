'''
@Author: rishi
'''


def findShortestSubArray(self, nums: List[int]) -> int:
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = [i]
        else:
            d[nums[i]].append(i)

    print(d)
    degree = 1

    for i in d:
        degree = max(degree, len(d[i]))

    print(degree)

    min_length = len(nums)
    for i in d:
        if len(d[i]) == degree:
            min_length = min(min_length, d[i][-1] - d[i][0] + 1)

    return min_length