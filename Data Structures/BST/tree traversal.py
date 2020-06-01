class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


def levelorder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while (len(q)>0):
        temp = q.pop(0)
        if temp:
            print(temp.data,end=" ")
            q.append(temp.left)
            q.append(temp.right)
        else:
            print("N",end=" ")



if __name__=='__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.right = node(7)

    inorder(root)
    print()
    preorder(root)
    print()
    postorder(root)
    print()
    levelorder(root)