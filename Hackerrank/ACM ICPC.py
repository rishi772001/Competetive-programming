#https://www.hackerrank.com/challenges/acm-icpc-team
a=[]
ip1=input().split(' ')
for i in range(int(ip1[0])):
	a.append(input())
o=[]
def calc(ar):
	de='00000'
	for i in ar:
		for j in range(len(i)):
			if(i[j]=='1'):
				de=de[:j]+'1'+de[(j+1):]
	c=de.count('1')
	return c
for d in range(len(a)):
	for f in range(d+1,len(a)):
		q=[]
		q.append(a[d])
		q.append(a[f])
		c=calc(q)
		o.append(c)

print(o)	
print(max(o))
print(o.count(max(o)))
		
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
