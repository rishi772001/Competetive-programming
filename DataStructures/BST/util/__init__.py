'''
@Author: rishi
'''

from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insert(node, root):
    if root is None:
        root = node
    else:
        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                insert(node, root.left)
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                insert(node, root.right)


def isleaf(node):
    if node.left is None and node.right is None:
        return True
    return False


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def height(root):
    if root:
        lht = height(root.left)
        rht = height(root.right)
        if lht >= rht:
            return lht + 1
        else:
            return rht + 1
    else:
        return 0


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def levelorder(root):
    if root is None:
        return
    q = list()
    q.append(root)
    while (len(q) > 0):
        temp = q.pop(0)
        if temp:
            print(temp.data, end=" ")
            q.append(temp.left)
            q.append(temp.right)


def levelorder_line_by_line(root):
    if root is None:
        return
    q = []
    q.append(root)
    while (len(q) > 0):
        s = len(q)
        for i in range(s):
            temp = q.pop(0)
            if temp:
                print(temp.data, end=" ")
                q.append(temp.left)
                q.append(temp.right)
        print()


def vertical_order(root):
    if root is None:
        return
    dist = defaultdict(list)
    q = list()
    q.append([root, 0])
    while len(q) > 0:
        s = len(q)
        for i in range(s):
            temp, lvl = q.pop(0)
            dist[lvl].append(temp.data)
            if temp.left:
                q.append([temp.left, lvl - 1])
            if temp.right:
                q.append([temp.right, lvl + 1])

    for i in sorted(dist):
        for j in dist[i]:
            print(j, end=" ")
        print()
