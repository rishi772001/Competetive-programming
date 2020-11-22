'''
@Author: rishi
https://cses.fi/problemset/task/1679
'''
from collections import defaultdict
n, m = map(int, input().split())
req = []
for _ in range(m):
    req.append(list(map(int, input().split())))

graph = defaultdict(list)
for i,j in req:
    graph[j].append(i)


visited = {}
for i in range(1, n+1):
    visited[i] = False

# i = 0 -> not visited, i = 1 -> visited, i = 2 -> processed
def detect_cycle(graph, visited, i):
    if visited[i] == 1:
        return True
    elif visited[i] == 2:
        return False
    else:
        visited[i] = 1
        for curr in graph[i]:
            if detect_cycle(graph,visited, curr):
                return True
        visited[i] = 2
    return False

def detect(graph, n):
    visited = {}
    for i in range(1, n + 1):
        visited[i] = 0
    for i in range(1, n+ 1):
        if visited[i] == 0:
            if detect_cycle(graph, visited, i):
                return True
    return False

def DFS(graph, visited, stack, i):
    visited[i] = True
    for curr in graph[i]:
        if not visited[curr]:
            DFS(graph, visited, stack, curr)
    stack.append(i)

if detect(graph, n):
    print("IMPOSSIBLE")
    exit(0)

stack = []
visited = {}
for i in range(1, n+1):
    visited[i] = False
for temp in range(1, n+1):
    if not visited[temp]:
        DFS(graph, visited, stack, temp)
for i in stack:
    print(i, end=" ")
