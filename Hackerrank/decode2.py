st=input()
key=int(input())
op=""
for i in st:
	if(at.count(i)==2):
		if(key>26):
			key=key%26
		
		op=op+(chr(ord(i)+key))
	else:
		if(key<)
		
		op=op+(chr(ord(i)-key))