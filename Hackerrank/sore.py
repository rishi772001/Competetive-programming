cal=int(input())
n=int(input())
ar=input().split(' ')
arr=[]
for i in ar:
	arr.append(int(i))
print(arr.index(cal))