class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_last(self,data):
        newnode=Node(data)
        if(self.head==None):
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def display(self):
        temp=self.head
        while(temp.next!=None):
            print(temp.data)
            temp=temp.next
        print(temp.data)
    def reverse(self):
        ar=[]
        temp=self.head
        while(temp.next!=None):
            ar.append(temp.data)
            temp=temp.next
        ar.append(temp.data)
        ar.reverse()
        return ar
a=int(input())

llist_array=linked()
for i in range(a):
    b=int(input())
    for j in range(b):
        llist_array.insert_last(int(input()))
    print(llist_array.reverse())

    
        
        
