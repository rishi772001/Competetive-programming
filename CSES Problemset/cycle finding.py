'''
@Author: rishi
https://cses.fi/problemset/task/1197
'''
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
ancestors = {}
for i in range(2, n + 1):
    distance[i] = 2**64
    ancestors[i] = None
distance[1] = 0
ancestors[1] = None


# Iterate for n - 1 times
for i in range(n-1):
    flag = True
    # Iterate through the edge list
    for src, dest, cost in edges:
        # Update if condition is true
        if distance[dest] > distance[src] + cost:
            flag = False
            distance[dest] = distance[src] + cost
            ancestors[dest] = src
    # if no updation in the last iteration the there will be no more updation
    if flag:
        break

# check for negative cycles
temp = None
for src, dest, cost in edges:
    if distance[dest] > distance[src] + cost:
        temp = dest


if temp:
    print("YES")
    ans = []
    while temp not in ans or ancestors[temp] == None:
        ans.append(temp)
        temp = ancestors[temp]
    ind = ans.index(temp)
    ans = ans[ind:]+[temp]
    for i in ans:
        print(i, end = " ")
else:
    print("NO")

