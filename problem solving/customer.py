class Node:
    def __init__(self,data,name,city,bal):
        self.data=data
        self.next=None
        self.name=name
        self.city=city
        self.bal=bal
class linked:
    def __init__(self):
        self.head=None
    def insert_first(self,data,name,city,bal):
        newnode=Node(data,name,city,bal)
        newnode.next=self.head
        self.head=newnode
    def insert_last(self,data,name,city,bal):
        newnode=Node(data,name,city,bal)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
    def insert_mid(self,data,name,city,bal):
        newnode=Node(data,name,city,bal)
        pos=int(input("enter"))
        temp=self.head
        count=1
        while count<pos:
            temp=temp.next
            count+=1
        newnode.next=temp.next
        temp.next=newnode
    def display(self,acc):
        
        temp=self.head
        while(acc!=temp.data):
            #print("Acc_No:",temp.data,",Name:",temp.name,",City:",temp.city,",Balance:",temp.bal)
            temp=temp.next
        print("Acc_No:",temp.data,",Name:",temp.name,",City:",temp.city,",Balance:",temp.bal)
    def delete(self):
        temp=self.head
        self.head=temp.next
    def delete_last(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def delete_mid(self,data):
        temp=self.head
        self.data=data
        
        while(self.data==temp):
            temp=temp.next
            count+=1
        temp.next=temp.next.next
    def size(self):
        count=0
        temp=self.head
        while(temp!=None):
            count+=1
            temp=temp.next
        print(count)
    def search(self,n):
        print("n",n)
        print("d",self.head.data)
        if(n==self.head.data):
            temp=self.head
            while(temp.next!=None):
                print(temp.data)
                temp=temp.next
            print(temp.data)
        else:
            print("Data Not Found")
        


ob=linked()
ob.insert_first(input("Enter Account Number"),input("Enter Name"),input("Enter City"),input("Enter Balance"))
print("<-------------------->")
ob.insert_last(input("Enter Account Number"),input("Enter Name"),input("Enter City"),input("Enter Balance"))
print("<-------------------->")
ob.insert_last(input("Enter Account Number"),input("Enter Name"),input("Enter City"),input("Enter Balance"))
print("<-------------------->")
ob.insert_last(input("Enter Account Number"),input("Enter Name"),input("Enter City"),input("Enter Balance"))
print("<-------------------->")
ob.insert_last(input("Enter Account Number"),input("Enter Name"),input("Enter City"),input("Enter Balance"))
print("<-------------------->")
ob.display(input("Enter Account Number to be Displayed"))            
