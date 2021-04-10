'''
@Author: rishi
'''


def reverse(a, x, y):
    for i in range(x, y // 2):
        a[i], a[y - i] = a[y - i], a[i]


a = [1, 2, 3, 4, 5, 6, 7]
k = 2

for i in range(0, len(a), k):
    reverse(a, i, i + k)

print(a)
