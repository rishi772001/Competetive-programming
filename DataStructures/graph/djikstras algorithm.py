'''
@Author: rishi
'''
from collections import defaultdict
from queue import Queue

n = 3
node_len = 4
nodes = [[1, 2, 6],
         [1, 3, 2],
         [3, 2, 3],
         [1, 3, 4]]
graph = defaultdict(list)
for i, j, k in nodes:
    graph[i].append([j, k])
    graph[j].append([i, k])
src = 1

# distance of nodes
dist = {}

q = Queue()

# dist from src to same node = 0 and add it to queue
dist[1] = 0
q.put([1, 0])
# dist from src to others node = infinity and add it to queue
for i in range(2, n + 1):
    dist[i] = 2 ** 32
    q.put([i, 2 ** 32])

while not q.empty():
    temp = q.get()
    node, distance = temp

    for crawl in graph[node]:
        dest, value = crawl
        if dist[node] + value < dist[dest]:
            dist[dest] = dist[node] + value

print(dist)