class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,node):
    if root is None:
        root=node
    else:
        if(node.data<root.data):
            if(root.left is None):
                root.left=node
            else:
                insert(root.left,node)
        else:
            if (root.right is None):
                root.right = node
            else:
                insert(root.right,node)

def levelorder(arr, root, i, n):
    if i<n:
        if(arr[i]!='N'):
            temp = node(arr[i])
            root = temp
            root.left = levelorder(arr, root.left, 2*i + 1, n)
            root.right = levelorder(arr, root.right, 2*i + 2, n)
        else:
            root = None
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

if __name__ == '__main__':
    root = None
    arr=[1,2,3,'N','N',4,6,'N',5,'N','N',7,'N']
    #arr=[2,'N',7,'N',6,'N',5,'N',9,'N',2,'N',6]
    root=levelorder(arr,root,0,len(arr))
    inorder(root)