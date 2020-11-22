'''
@Author: rishi
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(2**20)

n, m = map(int, input().split())
# routes = [[1, 2, 1],[1, 3, 3],[2, 3, 2],[2, 4, 6],[3, 2, 8],[3, 4, 1]]
routes = []
for i in range(m):
    routes.append(list(map(int, input().split())))

graph = defaultdict(list)
for i, j, k in routes:
    graph[i].append([j, k])

# print(graph)
visited = {}
for i in range(1, n+1):
    visited[i] = False

flights = []

mini = 2 ** 32

def find_mini(graph, visited, i, n, curr_flight, dist=0):
    global mini
    if i == n:
        if dist < mini:
            mini = dist
        return
    if not visited[i]:
        visited[i]= True
        for curr, val in graph[i]:
            find_mini(graph,visited,curr,n, curr_flight+1, dist+val)
        visited[i] = False
find_mini(graph, visited,1,n,0)


def DFS(graph, visited, i, n, curr_flight, dist=0):
    global mini
    if i == n:
        if dist < mini:
            mini = dist
            flights.append(curr_flight)
        elif dist == mini:
            flights.append(curr_flight)
        return
    if not visited[i]:
        visited[i]= True
        for curr, val in graph[i]:
            DFS(graph,visited,curr,n, curr_flight+1, dist+val)
        visited[i] = False

DFS(graph,visited,1,n,0)
print(mini, len(flights) % (10**9 + 7), min(flights), max(flights))
# print(flights)