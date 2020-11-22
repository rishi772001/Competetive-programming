class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        newnode=Node(data)
        self.head=newnode
        newnode.next=self.head
        
    def insert_mid(self,data):
        newnode=Node(data)
        pos=int(input("enter"))
        temp=self.head
        count=1
        while count<pos:
            temp=temp.next
            count+=1
        newnode.next=temp.next
        temp.next=newnode
    def insert_last(self,data):
        newnode=Node(data)
        if(self.head==None):
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
    def display(self):
        print("<--------->")
        temp=self.head
        while(temp.next!=self.head):
            print(temp.data)
            temp=temp.next
        print(temp.data)
    def delete(self):
        temp=self.head
        self.head=temp.next
        while(temp.next.next!=self.head):
            temp=temp.next
        temp.next=self.head
        
        
    def delete_last(self):
        temp=self.head
        while(temp.next.next!=self.head):
            temp=temp.next
        temp.next=self.head
    def delete_mid(self,data):
        temp=self.head
        self.data=data
        while(self.data!=temp.next.data):
            temp=temp.next
            
        temp.next=temp.next.next
ob=linked()
ob.insert_first(10)
ob.insert_last(20)
ob.insert_last(30)
ob.insert_last(40)
ob.insert_last(50)
ob.display()
ob.delete()
ob.delete_last()
ob.delete_mid(30)
ob.display()

