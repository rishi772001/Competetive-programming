# https://leetcode.com/problems/add-two-numbers-ii/
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head =newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode

    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def calculate(self, first, second):
        temp1 = first.head
        temp2 = second.head
        a = ""
        b = ""
        while temp1 and temp2:
            a += str(temp1.data)
            b += str(temp2.data)
            temp1 = temp1.next
            temp2 = temp2.next

        if(temp1 is None):
            while temp2:
                b += str(temp2.data)
                temp2 = temp2.next

        if (temp2 is None):
            while temp1:
                a += str(temp1.data)
                temp1 = temp1.next

        sum = str(int(a)+int(b))
        for i in sum:
            self.insert(int(i))




first = linkedlist()
first.insert(1)
first.insert(0)
first.insert(0)
second = linkedlist()
second.insert(1)
second.insert(0)
second.insert(0)
third = linkedlist()
third.calculate(first,second)
third.traverse()
