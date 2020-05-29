def func(arr,a):
	i=int(a[0])-1
	while i<int(a[1]):
		arr[i]=arr[i]+int(a[2])
		i+=1
	return arr
arr=[]
a=[]
input1=input().split(" ")
n=input1[0]
m=input1[1]
for i in range(int(n)):
	arr.append(0)
for i in range(int(m)):
	a.append(input().split(" "))
for i in range(int(m)):
	func(arr,a[i])
#print(arr)
print(max(arr))