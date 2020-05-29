a=[]
ip1=int(input())
for i in range(ip1):
	q=[]
	ip=input().split(' ')
	for i in ip:
		q.append(int(i))
	a.append(q)
i=0
j=len(a)-1
l=0
r=0
while(j>=0 and i<len(a)):
	r+=a[i][j]
	j-=1
	i+=1
i=0
while(i<len(a)):
	l+=a[i][i]	
	i+=1
'''print(l)
print(r)'''
print(abs(l-r))











