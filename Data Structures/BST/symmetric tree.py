class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


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


root = node(1)
root.left = node(2)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(4)
root.right.left = node(4)
root.right.right = node(3)
print(issymmetric(root))