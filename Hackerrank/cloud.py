'''i=input().split(" ")
n=int(i[0])
k=int(i[1])
arr=input().split(" ")
e=100
i=1
while(i<=n):
	if(int(arr[i-1])==1):
		e-=3
	else:
		e-=1
	if(i==0):
		break
	i=((i)+k)
print(e)'''
i=input().split(" ")
n=int(i[0])
k=int(i[1])
arr=input().split(" ")
e=100
i=1
flag=0
while(i!=1 or flag==0):
    if(int(arr[i-1])==1):
        e-=3
    else:
        e-=1
    if((i+k)<=n):
        i=i+k
    else:
        i=k-(n-i)
    flag+=1
print(e)