n=int(input())
a=[]

for i in range(n):
	a.append(int(input()))
for i in range(n):
	add=0
    for j in range(a[i]):
        add+=j
        if(add>=a[i]):
            break
 	print(j)