#Find the count of inner strings that starts and ends with a and b.
#I/P: aabb
#O/P: 4
a=input()
c=0
for i in range(len(a)):
	if(a[i]=='a'):
		for j in range(i,len(a)):
			if(a[j]=='b'):
				c+=1
print(c)
				
	
