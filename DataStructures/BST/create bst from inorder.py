

class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def construct_inorder(root, arr):
    n = len(arr)
    i = n // 2
    if (i > 0):
        root = node(arr[i])
        root.left = construct_inorder(root.left, arr[:n // 2])
        root.right = construct_inorder(root.right, arr[n // 2:])
    return root

def construct_preorder(root, arr):
    if (len(arr) > 0):
        root = node(arr[0])
        root.left = construct_preorder(root.left, arr[1:])
        root.right = construct_preorder(root.right, arr[1:])
    return root


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        root = None
        n = 5
        arr = [1, 2, 3, 4, 5]
        arr.insert(0, 0)
        root = construct_inorder(root, arr)
        preorder(root)
        print()
        arr.pop(0)
        root = construct_preorder(root, arr)
        preorder(root)

