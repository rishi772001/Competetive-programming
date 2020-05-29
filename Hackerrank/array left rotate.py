#https://www.hackerrank.com/challenges/circular-array-rotation
def rotate(list,n):
	return list[-n:]+list[:-n]
inpit=input().split(" ")
n=int(inpit[0])
k=int(inpit[1])
#q=int(inpit[2])
arr=input().split(" ")
list=rotate(arr,k)
for i in range(n):
	print(list[i])
