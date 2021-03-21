n = int(input())

a = input().split(" ")
max = a[0]
for i in range(n):
    if (a[i] > max):
        max = a[i]
        i = i + 1
value = a.count(max)
print(value)
