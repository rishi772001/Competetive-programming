'''
@Author: rishi
'''
a = [7,6,1,8,4,35,18]

for i in range(len(a)):
    index = i
    for j in range(i, len(a)):
        if a[j] < a[index]:
            index = j
    a[i], a[index] = a[index], a[i]
print(a)