'''
@Author: rishi
'''
from collections import defaultdict
from queue import PriorityQueue

n, node_len = map(int, input().split())
nodes = []
for i in range(node_len):
    nodes.append(list(map(int, input().split())))

graph = defaultdict(list)
for i, j, k in nodes:
    graph[i].append([j, k])
    # graph[j].append([i, k])

print(graph)

src = 1

# create distance array and queue
dist = {}
q = PriorityQueue()
array_q = []

# add infinite value to all other vertices except src vertex
dist[1] = 0
q.put(1)
array_q.append(1)
for i in range(2, n + 1):
    dist[i] = 2**32
    q.put(i)
    array_q.append(i)

# traverse until q is empty
while q.empty() == False:
    # current node
    u = q.get()
    array_q.remove(u)
    # traverse all neighbours of u
    for neighbour, distance in graph[u]:
        # update distance if curr_dist is less than the neighbour's distance
        # TODO: some mistake
        if dist[u] + distance < dist[neighbour] and dist[u] != 2**32 and neighbour in array_q:
            dist[neighbour] = dist[u] + distance

    print(dist)
# for i in dist:
#     print(dist[i], end=" ")