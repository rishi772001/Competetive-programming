#https://www.hackerrank.com/challenges/two-strings/problem

def calc():
	s1=input()
	s2=input()
	c=0
	for i in s1:
		if(i in s2):
			c+=1
		else:
			pass
	if(c>1):
		print("YES")
	else:
		print("NO")
n=int(input())
for i in range(n):
	calc()
