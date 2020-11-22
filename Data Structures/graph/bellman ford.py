'''
@Author: rishi
'''

n, edge_len = map(int, input().split())
# Get edge list
edges = []
for i in range(edge_len):
    edges.append(list(map(int, input().split())))
# create distance array with infinite except src vertex
distance = {}
for i in range(2, n + 1):
    distance[i] = -2**64
distance[1] = 0
# Iterate for n - 1 times
for i in range(1, n-1):
    flag = True
    # Iterate through the edge list
    for src, dest, cost in edges:
        # Update if condition is true
        if distance[dest] < distance[src] + cost:
            flag = False
            distance[dest] = distance[src] + cost
    # if no updation in the last iteration the there will be no more updation
    if flag:
        break

# check for negative cycles
for src, dest, cost in edges:
    if distance[dest] < distance[src] + cost:
        print(-1)
        exit(0)

for i in range(1, n+1):
    print(distance[i], end=" ")
