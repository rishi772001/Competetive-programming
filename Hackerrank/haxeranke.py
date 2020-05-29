def calc():
	s=input()
	st="hackerrank"
	j=0
	cnt=0
	for i in st:
		while(j<len(s)):
			if(i==s[j]):
				cnt+=1
				
				j+=1
				break
			else:
				
				j+=1
	if(cnt==10):
		print('YES')
	else:
		print('NO')
				
				
n=int(input())
for i in range(n):
	calc()
			
			
			
			
	
	
	
	
	
	
	
		