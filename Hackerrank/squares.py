def calc():	
	a=[]
	co=0
	for i in range(10000):
		a.append(i*i)
	inp=input().split(" ")
	b=int(inp[0])
	c=int(inp[1])
	for i in range(b,(c+1)):
		if(i in a):
			co+=1
	print(co)
inp1=int(input())
for i in range(inp1):
	calc()