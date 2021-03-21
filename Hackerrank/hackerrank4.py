input1 = input().split()
x1 = int(input1[0])
v1 = int(input1[2])
x2 = int(input1[1])
v2 = int(input1[3])

while (x1 < 10000):
    if (x1 == x2):
        print("YES")
    elif (x1 == 10001):
        print("NO")

    else:
        x1 = x1 + v1
        x2 = x2 + v2
