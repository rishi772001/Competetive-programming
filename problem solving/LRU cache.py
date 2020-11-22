'''
@Author: rishi
'''
from collections import OrderedDict


class LRUCache:

    def __init__(self, cap):
        self.cap = cap
        self.q = OrderedDict()

    # This method works in O(1)
    def get(self, key):
        if key not in self.q:
            return -1
        else:
            ans = self.q.pop(key)
            self.q[key] = ans
            return ans

    # This method works in O(1)
    def set(self, key, value):
        if key in self.q:
            self.q.pop(key)
            self.q[key] = value
        else:
            if len(self.q) == self.cap:
                self.q.popitem(last=False)

            self.q[key] = value
