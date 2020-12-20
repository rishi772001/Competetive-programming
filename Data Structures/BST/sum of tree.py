'''
@Author: rishi
'''


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def find(self, root):
        if root is None:
            return
        Solution.sum += root.val
        self.find(root.left)
        self.find(root.right)

    def solve(self, root):
        self.find(root)
        return Solution.sum


root = Tree(0)
root.left = Tree(1)
s = Solution()
print(s.solve(root))
