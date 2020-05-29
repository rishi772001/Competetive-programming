n=int(input())
st=input().split(" ")
ar=[]
for i in st:
	ar.append(int(i))
max=ar[0]
for i in ar:
	if(ar.count(i)>ar.count(max)):
		max=i
print(max)