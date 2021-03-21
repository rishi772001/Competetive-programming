i1=input().split(" ")
sp=input().split(" ")
n=int(i1[0])
m=int(i1[1])
array=[]
for i in range(n):
    array.append(i)
print(array)   
arr=[]
for i in range(n):
    ar=[]
    for j in sp:
        ar.append(i-int(array.index(j)))
    print(ar)
    print("i=",i,"j=",j,"j.index",sp.index(j))
