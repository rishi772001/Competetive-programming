'''
@Author: rishi
https://cses.fi/problemset/task/1750
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

def DFS(graph, src, k, count=0):
    if count >= k:
        return src
    for i in graph[src]:
        a = DFS(graph, i, k, count+1)
        if a != False:
            return a
    return False

for src, k in queries:
    print(DFS(graph, src, k), end=" ")
