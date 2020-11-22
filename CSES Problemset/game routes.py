'''
@Author: rishi
'''
from  collections import defaultdict
n, edge_len = map(int, input().split())
# Get edge list
edges = []
for i in range(edge_len):
    edges.append(list(map(int, input().split())))

graph = defaultdict(list)
for i, j in edges:
    graph[i].append(j)

# print(graph)
visited = {}
for i in range(1, n+1):
    visited[i] = False

count = 0
def DFS(graph, visited, n, i):
    global count
    if i == n:
        count += 1
        return True
    flag = True
    if not visited[i]:
        visited[i] = True
        for curr in graph[i]:
            if not DFS(graph, visited, n, curr):
                flag = False

        visited[i] = False
    if flag:
        return False
    return True


DFS(graph,visited,n,1)
print(count)