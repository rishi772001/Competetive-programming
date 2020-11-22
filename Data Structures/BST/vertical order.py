'''
@Author: rishi
'''
from collections import defaultdict

def vertical_order(root):
    if root is None:
        return
    dist = defaultdict(list)
    q = []
    q.append([root, 0])
    while (len(q)>0):
        s = len(q)
        for i in range(s):
            temp, lvl = q.pop(0)
            dist[lvl].append(temp.data)
            if temp.left:
                q.append([temp.left, lvl - 1])
            if temp.right:
                q.append([temp.right, lvl + 1])

    for i in dist:
        for j in dist[i]:
            print(j, end = "")
        print()