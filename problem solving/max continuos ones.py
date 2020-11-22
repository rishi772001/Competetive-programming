# https://leetcode.com/problems/max-consecutive-ones/

def findMaxConsecutiveOnes(nums):
    ans = 0
    curr = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr += 1
        else:
            ans = max(curr, ans)
            curr = 0
    return max(curr, ans)

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))