from DataStructures.util.Node import Node as node


class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
        self.head.prev = newnode

    def insert_last(self, data):
        newnode = node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

    def insert_middle(self, data):
        pos = int(input())
        count = 1
        temp = self.head
        while count < pos:
            count = count + 1
            temp = temp.next
        newnode = node(data)
        temp = newnode
        newnode.next = temp.next
        temp.next = newnode

    def traverse(self):
        temp = self.head
        print("frwd")
        while temp != None:
            print(temp.data)
            temp = temp.next
        print("rev")
        last = temp
        while last != None:
            print(last.data)
            last = last.prev

    def delete_first(self):
        if self.head == None:
            print("empty")
        else:
            temp = self.head
            self.head = temp.next

    def delete_last(self):
        if self.head == None:
            print("empty")
        else:
            temp = self.head
            prenode = self.head
            while (temp.next != None):
                temp = temp.next
            prenode.next = None

    def size(self):
        curr = self.head
        count = 0
        while (curr):
            count += 1
            curr = curr.next
        print(count)

    def search(self, data):
        curr = self.head
        while (curr):
            if curr.data == data:
                print("available")
            else:
                curr = curr.next
                print("not available")


s = linkedlist()
s.insert(10)
s.insert(50)
s.delete_first()
s.traverse()
