a="aabb"
c=0
for i in range(len(a)):
	if(a[i]=='a'):
		for j in range(i,len(a)):
			if(a[j]=='b'):
				c+=1
print(c)
				
	