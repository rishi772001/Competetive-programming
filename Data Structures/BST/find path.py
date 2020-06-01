class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def findPath(root, path, i=0):
    if i >= len(path):
        return True
    if root.data == path[i]:
        return (findPath(root.left, path, i + 1) or findPath(root.right, path, i + 1))
    else:
        return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inorder(root)
    print()
    path=[1, 2, 5]
    if(findPath(root, path)):
        print("Path Found")
    else:
        print("No Such Path")

