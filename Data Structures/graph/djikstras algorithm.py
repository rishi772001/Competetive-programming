'''
@Author: rishi
'''
from collections import defaultdict
from queue import PriorityQueue

n = 3
node_len = 4
nodes = [[1,2,6], [1, 3 ,2], [3 ,2, 3], [1, 3, 4]]
graph = defaultdict(list)
for i, j, k in nodes:
    graph[i].append([j, k])
    graph[j].append([i, k])
src = 1
dist = {}


q = PriorityQueue()

dist[1] = 0

q.put([1,0])

# h.heappush(q,[1, 0])

for i in range(2, n + 1):
    dist[i] = 2**32
    q.put([i, 2**32])

while q.empty() == False:
    temp = q.get()
    u = temp[0]

    for crawl in graph[u]:
        v = crawl[0]
        if dist[u] + crawl[1] < dist[crawl[0]]:
            dist[crawl[0]] = dist[u] + crawl[1]

print(dist)