n = int(input())
value = input()
values = value.split(" ")
count_best = 0
count_worst = 0
maxi = values[0]
mini = values[0]
for i in values:
    if (i > maxi):
        count_best += 1
        maxi = i
    if (i < mini):
        count_worst += 1
        mini = i

print(count_best, " ", count_worst)
