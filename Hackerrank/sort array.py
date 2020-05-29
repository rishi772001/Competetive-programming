input1=[13,2,4,15,12,10,5]
even=[]
odd=[]
for i in input1:
	if(input1.index(i)%2!=0):
		odd.append(i)
	else:
		even.append(i)
seven=even.sort()
sodd1=odd.sort()
sodd=sodd1.reverse()
print(sodd)
print(seven)
