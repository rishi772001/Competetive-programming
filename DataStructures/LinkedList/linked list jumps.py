'''
@Author: rishi
https://binarysearch.com/problems/Linked-List-Jumps
'''


def solve(self, node):
    mainnode = node

    while node is not None:
        i = 0
        temp = node

        while temp != None and i < node.val:
            temp = temp.next
            i += 1

        node.next = temp
        node = node.next

    return mainnode
