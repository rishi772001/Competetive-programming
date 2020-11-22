'''
@Author: rishi
https://cses.fi/problemset/task/1751
'''

from collections import defaultdict
import sys
sys.setrecursionlimit(2**20)

n = int(input())

teleport = {}
s = list(map(int, input().split()))
for i in range(1, n+1):
    teleport[i] = s[i - 1]


graph = defaultdict(list)
for i,j in teleport.items():
    graph[i].append(j)
# print(graph)

visited = {}
for i in range(1, n+1):
    visited[i] = False

def DFS(graph, vis, src, dist=0):
    if vis[src]:
        return dist
    vis[src] = True
    for i in graph[src]:
        a = DFS(graph, vis, i, dist + 1)
        if a:
            return a
    vis[src] = False
    return False


for src in range(1, n+1):
    visi = visited.copy()
    print(DFS(graph, visi, src), end = " ")

