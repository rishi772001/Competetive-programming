n=int(input())
a=input().split(" ")
b=[]
for i in a:
	b.append(int(i))
max=0
for i in b:
	if(max<i):
		max=i

print(b.count(max))