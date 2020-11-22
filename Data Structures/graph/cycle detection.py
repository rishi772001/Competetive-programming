'''
@Author: rishi
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
print(detect(graph, n))