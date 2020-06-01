class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def lca(root,n1,n2):
    if root is None:
        return None
    if root.data > n1 and root.data > n2 :
        return(lca(root.left,n1,n2))
    if root.data < n1 and root.data < n2 :
        return(lca(root.right,n1,n2))

    return root



if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    inorder(root)
    print()
    print(lca(root,10,22).data)