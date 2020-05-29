def rotate(liat,n):
	return liat[-n:]+liat[:-n]
inpit=input().split(" ")
n=int(inpit[0])
k=int(inpit[1])
#q=int(inpit[2])
arr=input().split(" ")
list=rotate(arr,k)
for i in range(n):
	print(list[i])
