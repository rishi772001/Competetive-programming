input1=input().split(" ")
n=input1[0]
k=input1[1]
input2=input().split(" ")
max=0
for i in input2:
	if(int(i)>max):
		max=int(i)
output=max-int(k)
if(output<0):
	output=0
print(output)