from pythonds.basic import Stack
s=Stack()
a=3
s.push(a)
t=4
cnt=1
while(a!=t):
	if(a==1):
		a=(s.pop())*2
		s.push(a)
	else:
		a-=1
	cnt+=1
print(cnt)
		
		
		
		
		
		
		
		
		
		
		
		