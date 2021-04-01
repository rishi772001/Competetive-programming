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
        carry = 0
        while first and second:
            s = str(first.data + second.data + carry)
            if len(s) > 1:
                carry = int(s[1:])
            self.insert(s[0])

            first = first.next
            second = second.next

        while first:
            s = str(first.data + carry)
            if len(s) > 1:
                carry = int(s[1:])
            self.insert(s[0])

            first = first.next

        while second:
            s = str(second.data + carry)
            if len(s) > 1:
                carry = int(s[1:])
            self.insert(s[0])

            second = second.next

        if carry > 0:
            carry = str(carry)
            for i in range(len(carry) - 1, -1, -1):
                self.insert(carry[i])


first = linkedlist()
first.insert(0)
first.insert(0)
first.insert(0)
first.insert(1)
second = linkedlist()
second.insert(0)
second.insert(0)
second.insert(1)

third = linkedlist()
third.calculate(first.head, second.head)
third.traverse()
