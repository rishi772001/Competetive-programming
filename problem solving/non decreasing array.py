# https://leetcode.com/problems/non-decreasing-array/submissions/
def checkPossibility(nums):
    c = 0               # Check for no of unsorted element
    ind = "None"        # Initially no index of unsorted element

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if c == 0:      # If this is the first unsorted element
                c = 1       # Change flag for visited unsorted element
                ind = i     # store index of unsorted element
            else:
                return False



    if ind != "None":           # If no unsorted element found return True
        a = nums.pop(ind)       # remove index to check for sorted array
    else:
        return True

    if nums == sorted(nums):    # remove index to check for sorted array
        return True
    else:
        nums.insert(ind, a)     # or else add index and remove index + 1 to check for sorted array
        nums.pop(ind + 1)
        if nums == sorted(nums):
            return True
    return False

print(checkPossibility([5,7,1,8]))