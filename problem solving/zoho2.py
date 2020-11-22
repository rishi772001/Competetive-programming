a=[2,4,5,6,7,9,10,13]
b=[2,3,4,5,6,7,8,9,11,15]
c=[]
for i in b:
    if(i in a):
        c= b.pop(i)
print(c)
