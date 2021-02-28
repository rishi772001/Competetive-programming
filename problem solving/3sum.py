'''
@Author: rishi
https://leetcode.com/problems/3sum/
'''


def three_sum(arr, k):
    arr.sort()
    ans = []
    for x in range(len(arr)):
        temp = [arr[x]]
        start = x + 1
        end = len(arr) - 1
        to_find = k - arr[x]
        while start < end:
            if arr[start] + arr[end] == to_find:
                temp += [arr[start], arr[end]]
                if temp not in ans:
                    ans.append(temp)
                temp = [arr[x]]
                start += 1
            elif arr[start] + arr[end] < to_find:
                start += 1
            else:
                end -= 1
    return ans


nums = [2, 0, 1]
k = 1
print(three_sum(nums, k))
