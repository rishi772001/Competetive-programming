'''
@Author: rishi
https://binarysearch.com/problems/Sum-of-Two-Numbers-Less-Than-Target
'''


def solve(nums, target):
    nums.sort()
    n = len(nums)

    start = 0
    end = n - 1

    ans = -987654321

    while start < end:

        val = nums[start] + nums[end]

        # Limit exceeded
        if val >= target:
            end -= 1

        if val < target:
            # Update ans if greater than previous ans
            ans = max(val, ans)
            # to find ans greater than current ans
            start += 1

    return ans
