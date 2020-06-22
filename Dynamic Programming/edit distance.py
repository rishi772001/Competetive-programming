# https://www.geeksforgeeks.org/edit-distance-dp-5/

s1 = "sunday"
s2 = "saturday"
n = len(s1)
m = len(s2)

arr = [[0 for i in range(m+1)] for i in range(n+1)]

for i in range(m+1):
    arr[0][i] = i

for i in range(n+1):
    arr[i][0] = i


for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]:
            arr[i][j] = arr[i-1][j-1]
        else:

            arr[i][j] = min(arr[i-1][j],arr[i][j-1],arr[i-1][j-1])+1


print(arr[n][m])
