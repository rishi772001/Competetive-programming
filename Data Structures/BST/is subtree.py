'''
@Author: rishi
'''


def check(self, root, target):
    if root is None or target is None:
        return root == target

    return root.val == target.val and self.check(root.left, target.left) and self.check(root.right, target.right)


def solve(self, root, target):
    if root is None:
        return root == target

    return self.solve(root.left, target) or self.solve(root.right, target) or self.check(root, target)