# https://leetcode.com/problems/same-tree/

class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None





def issame(root1, root2):
    if root1 and root2:
        if root1.data != root2.data:
            return False
        return issame(root1.left, root2.left) and issame(root1.right, root2.right)
    else:
        return root1 == root2

root1 = node(1)
root1.left = node(2)
root1.right = node(3)
root2 = node(1)
root2.left = node(2)
root2.right = node(3)
print(issame(root1, root2))
