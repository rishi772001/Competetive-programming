# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# https://www.youtube.com/watch?v=CE2b_-XfVDk -> reference vdo

# Input
arr = [3, 4, -1, 0, 6, 2, 3]
# dp array
dp = [1] * len(arr)

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
