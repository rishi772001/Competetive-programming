class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)



def insert(node, root):
    if (root == None):
        root = node
    else:
        if(node.data < root.data):
            if root.left is None:
                root.left = node
            else:
                insert(node, root.left)
        if (node.data > root.data):
            if root.right is None:
                root.right = node
            else:
                insert(node, root.right)


def postorder(root,arr):
    if root:
        postorder(root.left,arr)
        postorder(root.right,arr)
        arr.append(root.data)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    arr=[]
    postorder(root,arr)
    mainroot=Node(arr[0])
    arr.pop(0)
    for i in arr:
        insert(Node(i),mainroot)
    inorder(mainroot)