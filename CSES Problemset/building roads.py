'''
@Author: rishi
https://cses.fi/problemset/task/1666
'''

from collections import defaultdict as dic


cities,n = map(int, input().split())
roads = []
for i in range(n):
    roads.append(list(map(int, input().split())))

# print(roads)
# cities = 10
# roads = format_2d_int_list("2 5 5 6 1 4 6 8 2 6 3 6 1 10 8 9 2 3 5 8".replace(" ",","), 10, 2)
d = dic(list)
for i,j in roads:
    d[i].append(j)
    d[j].append(i)

visited = {}
for i in range(1, cities+1):
    visited[i] = False


ans = []
for i in range(1, cities+1):
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
        ans.append(temp)
# print(ans)
print(len(ans) - 1)

for i in range(len(ans) - 1):
    print(ans[i][0], ans[i+1][0])