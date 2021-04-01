# https://leetcode.com/problems/linked-list-cycle/
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



def traverse(node):
    temp=node
    while(temp):
        print(temp.data)
        temp=temp.next

# detects loop and remove it if present else return False
def detectLoop(node):
    s = set()
    temp = node
    while (temp):
        if (temp.next in s):
            temp.next = None
            return node
        s.add(temp)
        temp = temp.next
    return False

        # slow = self.head
        # fast = self.head
        # while fast and slow and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


if (detectLoop(node1)):
    traverse(node1)
    print("Loop found")
else:
    print("No Loop ")

# This code is contributed by Gitanjali.
