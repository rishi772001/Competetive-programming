'''
@Author: rishi
'''
import sys
from collections import defaultdict

n = int(input())

person = list(map(int, input().split()))

p = int(input())

pairs = []

for i in range(p):
    pairs.append(list(map(int, input().split())))

friends = defaultdict(list)

for i, j in pairs:
    friends[i].append(j)
    friends[j].append(i)

# print(friends)
groups = []

visited = {}
for i in range(1, n + 1):
    visited[i] = False

for i in range(1, n + 1):
    temp = set()
    if not visited[i]:
        q = [i]
        while q:
            val = q.pop(0)
            visited[val] = True
            temp.add(val)
            for curr in friends[val]:
                if not visited[curr]:
                    q.append(curr)
    groups.append(temp)
# print(groups)

ans = -sys.maxsize

for i in groups:
    s = 0
    for j in i:
        s += person[j - 1]
    ans = max(ans, s)

print(ans)
