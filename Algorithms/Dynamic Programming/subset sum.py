'''
@Author: rishi
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
https://www.youtube.com/watch?v=s6FhG--P7z0
'''


def solve(arr, total):
    dp = [[False] * (total + 1) for _ in range(len(arr))]

    # make first column true as 0 can be made by using all numbers
    for i in range(len(arr)):
        dp[i][0] = True

    # Make first row True only for that element
    dp[0][arr[0]] = True

    # i --> traverse row wise, j --> col wise
    for i in range(1, len(arr)):
        for j in range(1, total + 1):
            if arr[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - arr[i]] or dp[i - 1][j]
    return dp[-1][-1]


print(solve([2, 3, 7, 8, 10], 11))
