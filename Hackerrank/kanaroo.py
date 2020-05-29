a=input().split(' ')
i=int(a[0])
i1=int(a[1])
j=int(a[2])
j1=int(a[3])
for k in range(1000000):
	if(i==j):
		print("YES")
		exit()
	else:
		i+=i1
		j+=j1
print("NO")
	
	
	
	
	
	
	
	
	
	
	
		
	