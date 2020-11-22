# https://leetcode.com/problems/pascals-triangle/

def pascal(n):
    if n == 0:
        a = []
        return a
    elif n == 1:
        a = [[1]]
        return a
    elif n == 1:
        a = [[1], [1, 1]]
        return a
    else:
        a = [
            [1],
            [1, 1]
        ]
        for i in range(2, n):
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = a[i - 1][j - 1] + a[i - 1][j]
            a.append(temp)
        return a


print(pascal(5))