'''
@Author: rishi

detect cycle using graph coloring and if no cycle
then do topological sorting -> for any edge uv, u comes before v

1) DO dfs and push it stack at the end
2) print the stack
'''
from collections import defaultdict

n = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
graph = defaultdict(list)
for i, j in edges:
    graph[i].append(j)


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
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            if detect_cycle(graph, visited, i):
                return True
    return False


def DFS(graph, visited, stack, i):
    visited[i] = 1
    for curr in graph[i]:
        if not visited[i]:
            DFS(graph, visited, stack, curr)
    stack.append(i)

if detect(graph, n):
    print("-1")
    exit(0)
stack = []
visited = [0]*n
for temp in range(n):
    if not visited[temp]:
        DFS(graph, visited, stack, temp)
print(stack[::-1])