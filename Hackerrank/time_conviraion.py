input_string=input()
list=input_string.split(":")

hr=list[0]
min=list[1]

word=list[2]
a=word[2:]

sec=word[:2]

if(a=="AM"):
	if(hr=="12"):
		print("00:"+str(min)+":"+str(sec))
	else:
		print(str(hr)+":"+str(min)+":"+str(sec))
else:
	if(hr=="12"):
		print("12:"+str(min)+":"+str(sec))
	else:
		hr=12+int(hr)
		print(str(hr)+":"+str(min)+":"+str(sec))
	