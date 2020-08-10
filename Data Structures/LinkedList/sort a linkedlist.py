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

    def insert_middle(self, data):
        pos = int(input())
        count = 1
        temp = self.head
        while (count < pos):
            count = count + 1
            temp = temp.next
        newnode = node(data)
        temp = newnode
        newnode.next = temp.next
        temp.next = newnode

    def traverse(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

    def sort(self):
        n = self.size()

        for i in range(n):
            temp = self.head
            for j in range(0, n - i - 1):
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next

    def size(self):
        curr = self.head
        count = 0
        while (curr):
            count += 1
            curr = curr.next
        return count




s = linkedlist()
arr = [64, 34, 25, 12, 22, 11, 90]
for i in arr:
    s.insert(i)
s.sort()
s.traverse()



