a=input('Enter Name:')
b={}
for i in a:
	if(i in b.keys()):
		b[i]+=1
	else:
		b[i]=1
for key, value in sorted(b.items(),key=lambda item: item[1],reverse=True):
    print("%s: %s" % (key, value))