n=int(input())
s=input()
k=int(input())
k=k%26
p=""
for i in s:
	if(i.isalpha()):
		v=ord(i)
		if(i.isupper() and ((((v)+k)>90))):
			v=v-26
		if(i.islower() and ((((v)+k)>122))):
			v=v-26
		p+=chr(v+k)
	else:
		p+=i
print(p)
		