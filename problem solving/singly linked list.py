class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_last(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head =newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def insert_middle(self,data):
        pos=int(input())
        count=1
        temp=self.head
        while(count<pos):
            count=count+1
            temp=temp.next
        newnode=node(data)
        temp=newnode
        newnode.next=temp.next
        temp.next=newnode
    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def delete_first(self):
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            self.head=temp.next
    def delete_last(self):
        if self.head==None:
            print("empty")
        else:
            temp = self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next = None
    def size(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        print(count)
    def search(self,data):
        curr=self.head
        while(curr):
            if(curr.data==data):
                print("available")
            else:
                curr=curr.next
                print("not available")
s=linkedlist()
s.insert(10)
s.insert_last(50)
s.insert_last(100)
s.insert_last(150)
s.delete_last()
s.traverse()
            
            
            
