# https://www.geeksforgeeks.org/min-cost-path-dp-6/

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
r = len(cost[0])
c = len(cost)

arr = [[0 for i in range(r)] for i in range(c)]

m = 2
n = 2

arr[0][0] = cost[0][0]

for i in range(1,m+1):
    arr[i][0] = arr[i-1][0] + cost[i][0]

for i in range(1,n+1):
    arr[0][i] = arr[0][i-1] + cost[0][i]


for i in range(1,m+1):
    for j in range(1,n+1):
        arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + cost[i][j]

for i in arr:
    print(i)

print(arr[m][n])

