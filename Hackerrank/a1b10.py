#https://www.geeksforgeeks.org/zoho-interview-set-3-campus/
s=input()
a=[]
b=[]
last=1
for i in range(len(s)):
	if(s[i]>='0' and s[i]<='9'):
		if(last==1):
			a.append(int(s[i]))
		else:
			a[len(a)-1]=(a[len(a)-1]*10)+int(s[i])
		last=0
	else:
		b.append(s[i])
		if(last==1 and a!=[]):
			a.append(1)
		last=1
if(last==1):
	a.append(1)
c=""
for i in range(len(a)):
	for j in range(a[i]):
		c+=b[i]
print(c)
