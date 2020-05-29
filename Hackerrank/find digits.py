def calc():
	m=int(input())
	n=m
	a=[]
	count=0
	while(n>0):
		a.append(n%10)
		n=n//10
	for i in a:
		
		if(i!=0):
			
			if(m%i==0):
				count+=1
	print(count)
num=int(input())
for i in range(num):
	calc()