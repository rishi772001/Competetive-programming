'''
@Author: rishi
'''
from collections import defaultdict
from queue import PriorityQueue

n, node_len,query_len = map(int, input().split())
nodes = []
for i in range(node_len):
    nodes.append(list(map(int, input().split())))
queries = []
for i in range(query_len):
    queries.append(list(map(int, input().split())))
# print(nodes)
graph = defaultdict(list)
for i, j, k in nodes:
    graph[i].append([j, k])
    # graph[j].append([i, k])

# print(graph)
for x,y in queries:
    src = x
    dist = {}


    q = PriorityQueue()

    dist[1] = 0

    q.put(1)


    for i in range(2, n + 1):
        dist[i] = 2**32
        q.put(i)

    while q.empty() == False:
        temp = q.get()
        u = temp

        for crawl in graph[u]:
            v = crawl[0]
            if dist[u] + crawl[1] < dist[crawl[0]]:
                dist[crawl[0]] = dist[u] + crawl[1]

    print(dist[y])
