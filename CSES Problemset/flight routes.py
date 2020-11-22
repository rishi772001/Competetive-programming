'''
@Author: rishi
https://cses.fi/problemset/task/1196
'''
from collections import defaultdict
n, m, out = map(int, input().split())
# routes = [[1, 2, 1],[1, 3, 3],[2, 3, 2],[2, 4, 6],[3, 2, 8],[3, 4, 1]]
routes = []
for i in range(m):
    routes.append(list(map(int, input().split())))

graph = defaultdict(list)
for i, j, k in routes:
    graph[i].append([j, k])

print(graph)
visited = {}
for i in range(1, n+1):
    visited[i] = False

distance = []

def DFS(graph, i, n, visited, arr, d=0):
    if i == n:
        arr.append(d)
        return
    if visited[i] == False:
        visited[i] = True
        for curr, val in graph[i]:
            DFS(graph, curr, n, visited, arr, d+val)
        visited[i] = False


DFS(graph, 1, n, visited, distance)
distance.sort()
print(distance)
for i in range(out):
    print(distance[i], end =" ")
