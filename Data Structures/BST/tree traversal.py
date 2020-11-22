from collections import defaultdict


class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def isleaf(node):
    if node.left is None and node.right is None:
        return True
    return False

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)


def height(root):
    if root:
        lht = height(root.left)
        rht = height(root.right)
        if(lht >= rht):
            return lht + 1
        else:
            return rht + 1
    else:
        return 0



def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


def levelorder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while (len(q)>0):
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
    while (len(q)>0):
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

    for i in sorted(dist):
        for j in dist[i]:
            print(j, end=" ")
        print()




if __name__=='__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    root.right.left.right = node(8)
    root.right.right.right = node(9)

    print("inorder")
    inorder(root)
    print("\npreorder")
    preorder(root)
    print("\npostorder")
    postorder(root)
    print("\nlevel order")
    levelorder(root)
    print("\nlevel order line by line")
    levelorder_line_by_line(root)
    print("height")
    print(height(root))
    print("vertical order")
    vertical_order(root)
