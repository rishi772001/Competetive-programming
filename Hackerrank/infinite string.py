'''str=input()
arr=[]
for i in str:
	arr.append(i)
n=int(input())
narr=[]
j=0
count=0

for i in range(n):
	if(j==(len(arr))):
		j=0
	narr.append(arr[j])
	j+=1

for i in narr:
	if(i=='a'):
		count+=1
print(count)'''
s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n %len(s)].count("a"))