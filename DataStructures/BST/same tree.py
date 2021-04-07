# https://leetcode.com/problems/same-tree/


def issame(root1, root2):
    if root1 and root2:
        if root1.data != root2.data:
            return False
        return issame(root1.left, root2.left) and issame(root1.right, root2.right)
    else:
        return root1 == root2


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
print(issame(root1, root2))
