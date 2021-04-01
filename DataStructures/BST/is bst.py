class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isBST(node):
    return (isBSTUtil(node, -2**32, 2**32- 1))



def isBSTUtil(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))

def find_inorder(root):
    current = root
    stack = []
    ans = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif (stack):
            current = stack.pop()
            ans.append(current.data)
            current = current.right
        else:
            break
    return ans

def find_inorder_recur(root, inord = []):
    if root:
        inord = find_inorder_recur(root.left, inord)
        inord.append(root.data)
        inord = find_inorder_recur(root.right, inord)
    return inord

def is_bst_using_inorder(root):
    inord = find_inorder_recur(root)
    return sorted(inord) == inord


if __name__ == '__main__':
    root=Node(2)
    root.left=Node(1)
    root.right=Node(3)
    root.right.right = Node(5)
    if(isBST(root)):
        print("Yes")
    else:
        print("No")