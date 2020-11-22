#https://www.hackerrank.com/challenges/journey-to-the-moon/problem

from collections import defaultdict

n = 4
arr = [[0,2]]

d = defaultdict(list)
for i,j in arr:
    d[i].append(j)
    d[j].append(i)
print(d)
visited = [False for _ in range(n)]

country = []
for i in range(n):
    temp = []
    if not visited[i]:
        q = [i]
        visited[i] = True
        while q:
            curr = q.pop(0)
            visited[curr] = True
            temp.append(curr)
            for astronaut in d[curr]:
                if not visited[astronaut]:
                    q.append(astronaut)

    if len(temp) > 0:
        country.append(temp)


print(country)
