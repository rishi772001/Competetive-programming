from DataStructures.BST.util import *


def isleaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False


def hasonechild(node):
    if node.left != None and node.right == None:
        return 1
    elif node.left == None and node.right != None:
        return 2
    else:
        return 0


def hastwochild(node):
    if node.left is not None and node.right is not None:
        return True
    else:
        return False


# min value node in the right subtree
def inordersuccessor(root):
    min = root
    while root.left:
        min = root.left
        root = root.left
    return min


def delete(data, root):
    if root is None:
        return None
    elif root.data > data:
        root.left = delete(data, root.left)
    elif root.data < data:
        root.right = delete(data, root.right)
    else:
        if isleaf(root):
            root = None
        elif hasonechild(root) == 1:
            root = root.left
        elif hasonechild(root) == 2:
            root = root.right
        elif hastwochild(root):
            min = inordersuccessor(root.right)
            root.data = min.data
            root.right = delete(min.data, root.right)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(40)
    root.right = Node(70)
    root.right.left = Node(60)
    root.right.right = Node(80)
    print("before delete:")
    inorder(root)
    print()
    print("after delete:")
    delete(70, root)
    inorder(root)
