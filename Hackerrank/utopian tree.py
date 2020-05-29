def calc():
	p=int(input())
	ht=1
	for i in range(p):
		if(i%2==0):
			ht=ht*2
		else:
			ht+=1
	print(ht)
n=int(input())
for i in range(n):
	calc()