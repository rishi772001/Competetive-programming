'''
@Author: rishi
'''

from collections import defaultdict

array = ["12", "21", "1", "221", "21", "12", "21"]
x = "1221"

remaining = {}
count = defaultdict(int)

for i in array:
    count[i] += 1

for i in array:
    if i in x:
        ind = x.index(i)
        if ind == 0:
            remaining[i] = len(i)

result = 0
for i, j in remaining.items():
    rem = x[j:]
    if count[rem] >= count[i]:
        result += count[i]
print(result)
