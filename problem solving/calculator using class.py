class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
obj=cal(a,b)
print("choice list:")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.divide")
c=int(input("enter choice:"))
if c==1:
    print("sum is",obj.add())
elif c==2:
    print("subtract is",obj.sub())
elif c==3:
    print("product is",obj.mul())
elif c==2:
    print("divide is",obj.div())
