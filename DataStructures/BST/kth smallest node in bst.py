'''
@Author: rishi
'''
from DataStructures.BST.util import *


def kthSmallest(root):
    global k

    # Base case
    if (root == None):
        return None

    # Search in left subtree
    left = kthSmallest(root.left)

    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        return left

    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 0):
        return root

    # Else search in right subtree
    return kthSmallest(root.right)


def find_inorder(root, inorder=[]):
    if root:
        inorder = find_inorder(root.left, inorder)
        inorder.append(root.val)
        inorder = find_inorder(root.right, inorder)
    return inorder


def solve(root):
    # return find_inorder(root)[k]
    return kthSmallest(root)


root = Node(47)
root.left = Node(1)
root.left.right = Node(24)

k = 2
print(solve(root).data)
