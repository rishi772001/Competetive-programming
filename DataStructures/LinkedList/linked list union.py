'''
@Author: rishi
https://binarysearch.com/problems/Linked-List-Union
'''
from DataStructures.util.Node import Node as LLNode


def solve(self, ll0, ll1):
    new_llist = None
    if ll0 == None and ll1 == None:
        return new_llist

    while ll0 is not None and ll1 is not None:
        if ll0.val < ll1.val:
            if new_llist is None:
                new_llist = LLNode(ll0.val)
                head = new_llist
            else:
                new_llist.next = LLNode(ll0.val)
                new_llist = new_llist.next
            ll0 = ll0.next


        elif ll0.val > ll1.val:
            if new_llist is None:
                new_llist = LLNode(ll1.val)
                head = new_llist
            else:
                new_llist.next = LLNode(ll1.val)
                new_llist = new_llist.next
            ll1 = ll1.next

        else:
            if new_llist is None:
                new_llist = LLNode(ll1.val)
                head = new_llist
            else:
                new_llist.next = LLNode(ll1.val)
                new_llist = new_llist.next
            ll0 = ll0.next
            ll1 = ll1.next

    while ll0 is not None:
        if new_llist is None:
            new_llist = LLNode(ll0.val)
            head = new_llist
        else:
            new_llist.next = LLNode(ll0.val)
            new_llist = new_llist.next
        ll0 = ll0.next

    while ll1 is not None:
        if new_llist is None:
            new_llist = LLNode(ll1.val)
            head = new_llist
        else:
            new_llist.next = LLNode(ll1.val)
            new_llist = new_llist.next
        ll1 = ll1.next

    return head
