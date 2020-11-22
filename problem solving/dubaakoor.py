class Node:
    def __init__(self, v=None):
        self.data = v
        self.left = None
        self.right = None

def deserialize(root, s, i = 0):
    if root is None:
        root = Node(s[i])
    if i + 1 < len(s):
        deserialize(root.left, s, i + 1)
    if i + 2 < len(s):
        deserialize(root.left, s, i + 2)

root = None
s = "123"
deserialize(root, s)
