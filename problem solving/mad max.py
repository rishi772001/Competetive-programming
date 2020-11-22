'''
@Author: rishi
https://binarysearch.com/problems/Mad-Max
'''


def solve(nums, k):
    # n = len(nums)
    # q = []
    # max_val = []
    #
    # for i in range(k):
    #     q.append(nums[i])
    #
    # max_val.append(max(q))
    #
    # for i in range(k, n):
    #     q.pop(0)
    #     q.append(nums[i])
    #     max_val.append(max(q))
    #
    # return max_val

    n = len(nums)
    q = []
    max_val = []

    for i in range(k):
        q.append(nums[i])

    max_val.append(max(q))

    for i in range(k, n):
        val = q.pop(0)
        q.append(nums[i])
        if max_val[-1] != val:
            max_val.append(max(max_val[-1], nums[i]))

        else:
            max_val.append(max(q))


    return max_val


print(solve(nums = [10, 5, 2, 7, 8, 7],k = 3))