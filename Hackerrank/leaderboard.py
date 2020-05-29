
ip1=int(input())
sco=input().split(' ')
sco= list(map(int, sco)) 
ip3=int(input())
a=input().split(' ')

sc=[]
for i in sco:
	if(i not in sc):
		sc.append(i)
for i in a:
	i=int(i)
	sc.append(i)
	sc.sort(reverse=True)
	print(sc)
	print(sc.index(i)+1)
	sc.remove(i)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		