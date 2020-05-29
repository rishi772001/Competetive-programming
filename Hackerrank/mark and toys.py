ar=input().split(" ")
n=int(ar[1])
a=input().split(" ")
arr=[]
for i in a:
	arr.append(int(i))
#arr=[1,12,5,111,200,1000,10]
arr.sort()
#print(arr)
s=0
c=0
for i in range(len(arr)):
	if(s<=n):
		s+=int(arr[i])
		c+=1
	else:
		break
print(c-1)