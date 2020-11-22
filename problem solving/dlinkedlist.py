class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linked:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_last(self,data):
        newnode=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp.next
    def insert_mid(self,data):
        newnode=Node(data)
        pos=int(input("enter"))
        temp=self.head
        count=1
        while count<(pos):
            temp=temp.next
            count+=1
        newnode.prev=temp
        newnode.next=temp.next
        temp.next=newnode
        temp.next.prev=newnode
    def display(self):
        temp=self.head
        while(temp.next!=None):
            print(temp.data)
            temp=temp.next
        print(temp.data)
        print("<--------------------->")
    def delete_first(self):
        temp=self.head
        self.head=temp.next
    def delete_last(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def delete_mid(self,data):
        temp=self.head
        while(data!=temp.next.data):
            temp=temp.next
        temp.next=temp.next.next
        temp.next.prev=temp
        
ob=linked()
ob.insert_first(10)
ob.insert_last(20)
ob.insert_last(30)
ob.insert_last(40)
ob.insert_last(50)
ob.display()

ob.delete_mid(30)
ob.display()
