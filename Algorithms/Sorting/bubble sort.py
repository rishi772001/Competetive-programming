'''
@Author: rishi
'''

a = [7, 6, 1, 8, 4, 35, 18]

for i in range(len(a)):
    flag = True
    for j in range(1, len(a)):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = False
    # if no swap occurred then the array is sorted so break the remaining loops
    if flag:
        break
print(a)
