
inpit=input().split(" ")
k=int(inpit[0])
n=int(inpit[1])
a=input().split(" ")
rem=n-k
b=[]
for i in range(rem):
	b.append(a.pop())
b.sort()
print(b)
b+=a
print(b)