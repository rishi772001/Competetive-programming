inp1=input().split(" ")
inp2=input().split(" ")
d1=int(inp1[0])
m1=int(inp1[1])
y1=int(inp1[2])
d2=int(inp2[0])
m2=int(inp2[1])
y2=int(inp2[2])
fine=0
if(y1<=y2):
	if(m1<=m2):
		if(d1<=d2):
			fine+=0
		else:
			fine+=(15*(d2-d1))
	else:
		fine+=(500*(m2-m1))
else:
	fine+10000
print(abs(fine))