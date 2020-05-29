#https://www.hackerrank.com/challenges/ctci-ransom-note/problem
inp=input()
st1=input().split(" ")
c=0
st2=input().split(" ")
for i in st2:
	if(i in st1):
		c+=1
	else:
		pass
#print(c)
if(c==len(st2)):
	print("Yes")
else:
	print("No")
