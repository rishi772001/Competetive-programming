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
            print(temp.data, end=" ")
            temp = temp.next

    def size(self):
        curr = self.head
        count = 0
        while (curr):
            count += 1
            curr = curr.next
        print(count)

    def merge2list(self, b, c):
        a = linkedlist()
        btemp = b.head
        ctemp = c.head
        # i = b, j = c

        while btemp and ctemp:
            if (btemp.data <= ctemp.data):
                a.insert(btemp.data)
                btemp = btemp.next
            else:
                a.insert(ctemp.data)
                ctemp = ctemp.next



        if (btemp is None):  # Add remaining elements from c to a array
            while ctemp:
                a.insert(ctemp.data)
                ctemp = ctemp.next
        else:  # Add remaining elements from b to a array
            while btemp:
                a.insert(btemp.data)
                btemp = btemp.next
        return a

    def mergeksortedlist(self, arr):
        k = len(arr)
        if k == 1:
            return arr[0]
        elif k == 2:
            return self.merge2list(arr[0], arr[1])
        else:
            a = arr[:k // 2]
            b = arr[k // 2:]

            return self.merge2list(self.mergeksortedlist(a), self.mergeksortedlist(b))



a = linkedlist()
b = linkedlist()
c = linkedlist()
a.insert(1)
a.insert(4)
a.insert(5)

b.insert(1)
b.insert(3)
b.insert(4)

c.insert(2)
c.insert(6)
arr = [a,b,c]

out = a.mergeksortedlist(arr)
out.traverse()
