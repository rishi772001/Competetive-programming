# https://binarysearch.com/problems/Linked-List-Intersection

class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def solve(self, l0, l1):
        if l0 is None or l1 is None:
            return None
        out = None
        temp = None

        while l0 and l1:
            if l0.val == l1.val:
                if out is not None:
                    temp.next = LLNode(l0.val)
                    temp = temp.next
                else:
                    out = LLNode(l0.val)
                    temp = out
                l0 = l0.next
                l1 = l1.next
            while l0 and l1 and l0.val < l1.val:
                l0 = l0.next
            while l0 and l1 and l0.val > l1.val:
                l1 = l1.next
            if l1 is None or l0 is None:
                return out

        return out
