from DataStructures.BST.util import *


def isBST(node):
    return isBSTUtil(node, -2 ** 32, 2 ** 32 - 1)


def isBSTUtil(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


def find_inorder(root, inord=[]):
    if root:
        inord = find_inorder(root.left, inord)
        inord.append(root.data)
        inord = find_inorder(root.right, inord)
    return inord


def is_bst_using_inorder(root):
    inord = find_inorder(root)
    return sorted(inord) == inord


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.right.right = Node(5)
    if isBST(root):
        print("Yes")
    else:
        print("No")
