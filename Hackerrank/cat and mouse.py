def calc():	
	inpit=input().split(" ")
	cata=int(inpit[0])
	catb=int(inpit[1])
	mouse=int(inpit[2])
	value1=mouse-cata
	if(value1<0):
		value1=value1*(-1)
	value2=mouse-catb
	if(value2<0):
		value2=value2*(-1)
	if(value1<value2):
		print("Cat A")
	elif(value1>value2):
		print("Cat B")
	else:
		print("Mouse C")
q=int(input())
for i in range(q):
	calc()
	i+=1