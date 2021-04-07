'''
@Author: rishi
'''
from DataStructures.BST.util import *


def tree_to_str(root):
    if not root:
        return ''
    ans = str(root.val)
    l = tree_to_str(root.left)
    r = tree_to_str(root.right)
    if l and r:
        ans += '[' + l + ']' + '[' + r + ']'
    elif l and not r:
        ans += '[' + l + ']'
    elif not l and r:
        ans += '[][' + r + ']'
    return ans


def create(arr, root, i, n):
    if i < n:
        if arr[i] != 'N':
            temp = Node(arr[i])
            root = temp
            root.left = create(arr, root.left, 2 * i + 1, n)
            root.right = create(arr, root.right, 2 * i + 2, n)
        else:
            root = None
    return root


def str_to_tree(s):
    if s == '':
        return None

    s = s.replace("[]", "N").replace("[", "").replace("]", "")

    root = None
    return create(s, root, 0, len(s))


# 1[2[][4]][3]
# 12N43

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.right = Node(4)

"""

        1
    2       3
N       4

"""
print(tree_to_str(node))
preorder(str_to_tree("1[2[][4]][3]"))
