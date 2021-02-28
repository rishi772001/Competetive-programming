def calculate(n):
    arr = [0] * (n + 2)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    return arr[n]


test = int(input())

for i in range(test):
    n = int(input())
    print(calculate(n + 1))
