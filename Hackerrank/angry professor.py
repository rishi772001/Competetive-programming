def calc():
	inpit1=input().split(" ")
	n=inpit1[0]
	k=inpit1[1]
	arr=input().split(" ")
	late_count=0
	for i in arr:
		if(int(i)<=0):
			late_count+=1
	if(late_count>=int(k)):
		print("NO")
	else:
		print("YES")
	
a=int(input())
for i in range(a):
	calc()	
	
	
	
	
	