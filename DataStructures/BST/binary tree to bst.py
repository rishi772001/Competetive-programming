from DataStructures.BST.util import *


def storeInorder(root, inorder):
    if root is None:
        return

    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


def arrayToBST(arr, root):
    # Base Case
    if root is None:
        return

    # First update the left subtree
    arrayToBST(arr, root.left)

    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)

    # Finally update the right subtree
    arrayToBST(arr, root.right)


def binaryTreeToBST(root):
    if root is None:
        return

    # Create the temp array and store the inorder traveral of tree
    arr = []
    storeInorder(root, arr)
    # Sort the array
    arr.sort()
    # copy array elements back to binary tree
    arrayToBST(arr, root)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    binaryTreeToBST(root)

    inorder(root)
