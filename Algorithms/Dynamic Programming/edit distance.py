# https://www.geeksforgeeks.org/edit-distance-dp-5/

s1 = "draw"
s2 = "dew"
n = len(s1)
m = len(s2)

arr = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        # Fill base cases
        if i == 0:
            arr[i][j] = j
        elif j == 0:
            arr[i][j] = i

        # Recurrence relation
        # Same characters copy from top left diagonal
        elif s1[i - 1] == s2[j - 1]:
            arr[i][j] = arr[i - 1][j - 1]
        # else calc min(top, left, top left diagonal) + 1
        else:
            arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1


print(arr[n][m])
