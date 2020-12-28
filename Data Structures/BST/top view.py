'''
@Author: rishi
'''
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_order(root):
    if root is None:
        return
    dist = {}
    q = []
    q.append([root, 0])
    while (len(q)>0):
        s = len(q)
        for i in range(s):
            temp, lvl = q.pop(0)
            if lvl not in dist:
                dist[lvl] = temp.data
            if temp.left:
                q.append([temp.left, lvl - 1])
            if temp.right:
                q.append([temp.right, lvl + 1])

    for i in dist:
        print(dist[i][0])