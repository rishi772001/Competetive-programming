from DataStructures.BST.util import *


def isopposite(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    if root1.data != root2.data:
        return False
    else:
        return isopposite(root1.left, root2.right) and isopposite(root1.right, root2.left)


def issymmetric(root):
    if root is None:
        return True
    return isopposite(root.left, root.right)


def issymmetric_using_level_order_palindrome_checker(self, root):
    if root is None:
        return True
    q = []
    q.append(root)

    while q:
        size = len(q)
        temp = []
        for i in range(size):
            a = q.pop(0)
            if a is not None:
                temp.append(a.val)

                q.append(a.left)
                q.append(a.right)
            else:
                temp.append(-1)

        if temp != temp[::-1]: return False
    return True


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(issymmetric(root))
