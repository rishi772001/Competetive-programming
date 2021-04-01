class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = Node(data, self.head)

    def insert_values(self, lst_values):
        for i in lst_values:
            self.insert_at_end(i)

    def print(self):
        if self.head is None:
            print("The linked list is empty")
            return
        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + '__>'
            itr = itr.next
        print(lst)


g = CircularLinkedlist()
g.insert_values(["45", "45", "23", "89", "98", "55"])
g.print()