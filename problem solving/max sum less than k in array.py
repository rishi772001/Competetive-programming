'''
@Author: rishi
'''


def solve(nums, k):
    if (nums == None or nums.length == 0):
        return []

    # Step 1 sort the array
    nums.sort()

    # Step 2 Define ur pointers int
    start = 0
    end = len(nums) - 1

    # Step 3 define ur result int

    maxSum = -9876543219
    result = [None, None]

    # Step 4 Loop through the array Start < end because
    # we dont want to double traverse it(that is dumb af)

    while start < end:
        currentSum = nums[start] + nums[end]  # step 5

        if k < currentSum > maxSum:  # step 6
            maxSum = currentSum
            result[0] = start  # update result and store index
            result[1] = end

        if currentSum < k:  # sum is very small than k
            start += 1
        else:
            end -= 1  # sum is greater than k
    return result
