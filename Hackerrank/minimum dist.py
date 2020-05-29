ar=[]
n=int(input())
s=input().split(" ")
for i in s:
	ar.append(int(i))
max=[]
for i in range(len(ar)):
	count=0
	for j in range(i+1,len(ar)):
		count+=1
		if(ar[i]==ar[j]):
			max.append(count)
if(len(max)==0):
	print("-1")
else:			
	print(min(max))