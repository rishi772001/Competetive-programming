'''
@Author: rishi
https://cses.fi/problemset/task/1669
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1500)


n, m =list(map(int, input().split()))
connections = []
for i in range(m):
    connections.append(list(map(int, input().split(" "))))
connect = defaultdict(list)
for i,j in connections:
    connect[i].append(j)
    connect[j].append(i)

def DFS(d, ind, end, visited, flag, path = []):
    if flag and ind == end and len(path) > 1:
        return path
    flag = True
    visited[ind] = True
    for i in d[ind]:
        if not visited[i]:
            ans = DFS(d, i, end, visited,flag, path+[str(i)])
            if ans != -1:
                visited[ind] = False
                return ans
        elif i == end and len(path) > 1:
            visited[ind] = False
            return path
    visited[ind] = False
    return -1


visited = {}
for i in range(1, n+1):
    visited[i] = False

for i in range(1, n+1):
    ans = DFS(d=connect, ind=i, end=i,flag=False,visited=visited)
    if ans == -1:
        continue
    else:
        ans.insert(0, str(i))
        ans.append(str(i))
        print(len(ans))
        print(" ".join(ans))
        break
else:
    print("IMPOSSIBLE")