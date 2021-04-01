'''
@Author: rishi

cycle detection using Disjoint Set Union Find
Only for Undirected graph
Time Complexity : O(E * V)
https://www.youtube.com/watch?v=eTaWFhPXPz4
'''


# return true if both are present in the same set  --> O(N)
def find(set, src, dest):
    while set[src] != -1:
        src = set[src]
    while set[dest] != -1:
        dest = set[dest]
    return src == dest


# union of two sets is done by adding a edge --> O(N)
def union(set, src, dest):
    while set[src] != -1:
        src = set[src]
    while set[dest] != -1:
        dest = set[dest]
    set[src] = dest


def detect_cycle(v, e, edges):
    set = [-1] * v  # disjoint set containing all vertices with itself as root
    for src, dest in edges:
        if find(set, src, dest):
            return True
        else:
            union(set, src, dest)
    return False


E = 2
V = 3
edges = [
    [0, 1],
    [1, 2],
    [2, 0]
]
if detect_cycle(V, E, edges):
    print("Cycle found")
else:
    print("No cycle found")
