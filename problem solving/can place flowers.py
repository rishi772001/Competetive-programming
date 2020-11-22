# https://leetcode.com/problems/can-place-flowers/
def find(a, n):
    if len(a) == 1 and a[0] == 0:
        if n <= 1:
            return True
        else:
            return False

    if len(a) == 2 and a[0] == 0 and a[1] == 0 and n <= 1:
        return True

    if a[0] == 0 and a[1] == 0:
        a[0] = 1
        n -= 1

    for i in range(1, len(a) - 1):
        if a[i] == 0 and a[i - 1] == 0 and a[i + 1] == 0:
            a[i] = 1
            n -= 1

    if a[-1] == 0 and a[-2] == 0:
        n -= 1
    return n <= 0


a = [0,1,0,0,1]
n = 1
print(find(a,n))
