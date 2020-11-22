'''
@Author: rishi
https://cses.fi/problemset/task/1160
'''

from collections import defaultdict
import sys
sys.setrecursionlimit(2**20)

n,q = map(int, input().split())

teleport = {}
s = list(map(int, input().split()))
for i in range(1, n+1):
    teleport[i] = s[i - 1]

queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))


graph = defaultdict(list)
for i,j in teleport.items():
    graph[i].append(j)
# print(graph)

vis = {}
for i in range(1, n+1):
    vis[i] = False

def DFS(graph, src, k, dist=0):
    global count
    if src == k:
        if dist < count:
            count = dist
        return
    if not vis[src]:
        vis[src] = True
        for i in graph[src]:
            DFS(graph, i, k, dist + 1)
        vis[src] = False

for src, k in queries:
    count = 2 ** 32
    DFS(graph, src, k)
    if count == 2**32:
        print(-1)
    else:
        print(count)
