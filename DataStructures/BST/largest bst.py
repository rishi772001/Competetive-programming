'''
@Author: rishi
https://binarysearch.com/problems/Largest-Binary-Search-Subtree
'''
from DataStructures.BST.util import *

class find_inorder:
    def __init__(self):
        self.inord = []

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inord.append(root.val)
            self.inorder(root.right)


class Solution:
    def __init__(self):
        self.maxi = [0, None]

    def isbst(self, root):
        a = find_inorder()
        a.inorder(root)
        inord = a.inord
        return [sorted(inord) == inord, len(inord)]

    def find(self, root):
        if root:
            temp = self.isbst(root)
            print(temp, self.maxi)
            if temp[0]:
                if self.maxi[0] < temp[1]:
                    self.maxi[0] = temp[1]
                    self.maxi[1] = root

            self.find(root.left)
            self.find(root.right)

    def solve(self, root):
        self.find(root)
        return self.maxi[1].val


node = Node(1)
node.left = Node(3)
node.left.left = Node(2)
node.left.right = Node(5)
s = Solution()
print(s.solve(node))
