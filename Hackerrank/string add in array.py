a=[1,3,4,5,8]
b=[1,2,3,6,7]
for i in b:
	if i not in a:
		a.append(i)
a.sort()
print(a)	