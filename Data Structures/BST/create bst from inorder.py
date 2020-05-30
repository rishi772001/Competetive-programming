class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def construct(root, arr):
    n = len(arr)
    i = n // 2
    if (i > 0):
        root = node(arr[i])
        root.left = construct(root.left, arr[:n // 2])
        root.right = construct(root.right, arr[n // 2:])
    return root


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        root = None
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr.insert(0, 0)
        root = construct(root, arr)
        preorder(root)
