ar=input().split(" ")
p=int(ar[0])
d=int(ar[1])
m=int(ar[2])
s=int(ar[3])
count=0
op=0
while True:
	if(count>=s):
		break
	else:
		count+=p
		if(p>=m):
			p-=d
		op+=1
	

print(op-1)