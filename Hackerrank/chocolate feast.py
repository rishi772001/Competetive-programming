def calc(ar):
	n=int(ar[0])
	c=int(ar[1])
	m=int(ar[2])
	wrapper=n//c
	ate=n//c
	while(wrapper>=m):
		ate+=1
		wrapper-=m
		wrapper+=1
	
	print(ate)
	
	
	
c=int(input())
for i in range(c):
	ar=input().split(' ')	
	calc(ar)
	
	
	
	