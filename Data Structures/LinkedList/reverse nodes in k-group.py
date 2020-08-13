#https://leetcode.com/problems/reverse-nodes-in-k-group/
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newnode

    def traverse(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next


def reverseList(head, k):
    if head is None:
        return None
    curr = head
    prev = None
    next = None
    count = 0
    while (curr and count < k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    if next is not None:
        head.next = reverseList(next, k)

    return prev






s = linkedlist()
arr = [1,2,3,4,5,6,7,8,9]
for i in arr:
    s.insert(i)
s.head = reverseList(s.head,3)
s.traverse()