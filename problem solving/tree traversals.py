def preOrder(root):
    if root:
        print(str(root.info) + " ", end="")  # for printing in same line
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.info) + " ", end="")
        inOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.info) + " ", end="")
