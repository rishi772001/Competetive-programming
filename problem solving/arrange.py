
    
   
a = []
n=int(input("enter limit"))
for i in range(n):
    a.append(int(input("Enter Number")))
count=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count=count+1
    break
print(count)

