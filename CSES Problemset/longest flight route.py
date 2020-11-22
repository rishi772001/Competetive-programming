'''
@Author: rishi
https://cses.fi/problemset/task/1680
'''
# from QuickDS import format_2d_int_list

from collections import defaultdict
import sys
sys.setrecursionlimit(2**20)

def DFS(graph, n, visited, i = 1, d = 0, path = ""):
    if i == n:
        return [d, path]

    flag = False
    if not visited[i]:
        visited[i] = True
        array = []
        for curr in graph[i]:
            a = DFS(graph, n, visited, curr, d + 1, path +" "+ str(curr))
            if not a or a == [d, path]:
                continue
            else:
                flag = True
                array.append(a)
        visited[i] = False

    if flag:
        mini = array[0][0]
        d, path = array[0]
        for p, q in array:
            if p > mini:
                d, path = p, q
        return [d, path]
    else:
        return False





n, m =list(map(int, input().split()))
connections = []
for i in range(m):
    connections.append(list(map(int, input().split(" "))))
connect = defaultdict(list)
for i,j in connections:
    connect[i].append(j)
# print(connect)

visited = {}
for i in range(1, n+1):
    visited[i] = False

# {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]})
ans = DFS(connect, n, visited)
if ans == False:
    print("IMPOSSIBLE")
else:
    print(ans[0] + 1)
    print('1' + " ".join(ans[1].split(" ")))

