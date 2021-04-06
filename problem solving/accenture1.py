'''
@Author: rishi
'''


def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def func(z):
    if z == 1:
        return 0
    if isprime(z):
        return 1

    if z % 2 == 0:
        x = 2
        y = z // 2
    else:
        for i in range(2, z):
            for j in range(i, z):
                if i * j == z and 1 < i <= j:
                    x = i
                    y = j
    return (y * func(x)) + (x * func(y))


def calc(n):
    temp = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            temp += func(i)
    temp += func(n)
    return temp


def strange_sum(L, R):
    s = 0
    for i in range(L, R + 1):
        s += calc(i)
    return s


T = int(input())
for _ in range(T):
    L, R = list(map(int, input().split()))

    out_ = strange_sum(L, R)
    print(out_)
