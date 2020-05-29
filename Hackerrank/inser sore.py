def pr(ar):
	s=" "
	print(s.join(ar))
	

ar=[]
n=int(input())
s=input()
for i in s:
	ar.append(int(i))
	
	
val=ar[len(ar)-1]
i=len(ar)-2
while(i>=0):
	if(ar[i]>val):
		ar[i+1]=ar[i]
		pr(ar)
	else:
		break
	i-=1
ar[i+1]=val
pr(ar)
	
	
	
















