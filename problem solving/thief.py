# https://practice.geeksforgeeks.org/problems/thief-try-to-excape/0
t = int(input())

while(t > 0):
    x,y,n = map(int, input().split())

    ht = list(map(int, input().split()))

    jumps = 0

    for i in ht:
        temp = i
        while temp>0:
            if temp == x:
                jumps += 1
                temp -= x
                break
            temp -= (x - y)
            jumps += 1
    print(jumps)