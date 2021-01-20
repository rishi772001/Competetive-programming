'''
@Author: rishi
https://www.geeksforgeeks.org/longest-common-substring-dp-29/
'''


def lcs(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range((len(s1) + 1))]
    maxi = -987654321

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                maxi = max(maxi, dp[i][j])

    return maxi


print(lcs("abcd", "bcdabdabcdlkd"))
