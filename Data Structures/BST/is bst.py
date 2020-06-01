class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isbst(root):
    if(root == None):
        return True
    if(isless(root.data, root.left) and isgreat(root.data, root.right) and isbst(root.left) and isbst(root.right)):
        return True
    else:
        return False

def isless(data,root):
    if root is None:
        return True
    if(root.data < data and isless(data,root.left) and isless(data,root.right)):
        return True
    else:
        return False

def isgreat(data,root):
    if root is None:
        return True
    if(root.data > data and isgreat(data,root.left) and isgreat(data,root.right)):
        return True
    else:
        return False

if __name__ == '__main__':
    root=Node(2)
    root.left=Node(1)
    root.right=Node(3)
    if(isbst(root)):
        print("Yes")
    else:
        print("No")