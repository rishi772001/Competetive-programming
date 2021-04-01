'''
@Author: rishi
'''


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_inorder(root, inorder=[]):
    if root:
        inorder = find_inorder(root.left, inorder)
        inorder.append(root.val)
        inorder = find_inorder(root.right, inorder)
    return inorder


def solve(root, k):
    print(find_inorder(root))
    return find_inorder(root)[k]


root = Tree(47)
root.left = Tree(1)
root.left.right = Tree(24)
print(find_inorder(root))
