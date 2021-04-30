# https://binarysearch.com/problems/Inverted-Subtree

from DataStructures.util.TreeNode import *


class Solution:
    def check(self, root, target):
        if root is None:
            return root == target

        if not root.left and not root.right:
            return not target.left and not target.right

        if root.left and not root.right:
            if target.left is None:
                return target.right and target.right.val == root.left.val and self.check(root.left, target.right)
            else:
                return not target.right and target.left.val == root.left.val and self.check(root.left, target.left)

        if root.right and not root.left:
            if target.left is None:
                return target.right and target.right.val == root.right.val and self.check(root.right, target.right)
            else:
                return not target.right and target.left.val == root.right.val and self.check(root.right, target.left)

        if not target.left or not target.right:
            return False

        if root.left.val == target.left.val and root.right.val == target.right.val:
            if self.check(root.left, target.left) and self.check(root.right, target.right):
                return True

        if root.left.val == target.right.val and root.right.val == target.left.val:
            return self.check(root.left, target.right) and self.check(root.right, target.left)

        return False

    def solve(self, source, target):
        if not source and not target:
            return True
        if (source and not target) or (target and not source):
            return False

        # find source in target
        q = []
        q.append(target)
        while q:
            temp = q.pop(0)
            if temp.val == source.val:
                to_find = temp
                if self.check(to_find, source):
                    return True
            if (temp.left):
                q.append(temp.left)
            if (temp.right):
                q.append(temp.right)
        return False


src = TreeNode(0)
src.left = TreeNode(1)
src.right = TreeNode(2)
src.left.right = TreeNode(3)

target = TreeNode(5)
target.left = TreeNode(2)
target.right = TreeNode(0)
target.right.left = TreeNode(2)
target.right.right = TreeNode(1)
target.right.right.left = TreeNode(3)

print(Solution().solve(src, target))
