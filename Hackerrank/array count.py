#Print count of each element of a in b
n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
	a.append(input())
m=int(input())
for i in range(m):
	b.append(input())
for i in b:
	c.append(a.count(i))
for i in c:
	print(i)
