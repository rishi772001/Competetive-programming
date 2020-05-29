def calc(List): 

    return max(set(List), key = List.count) 
n=int(input())
s =input().split(" ")
ar=[]
for i in s:
	ar.append(int(i))

max=calc(ar)
ar[:] = (value for value in ar if value != max)
print(len(ar))