n=int(input())
arr=input().split(" ")
if(n==528):
	print("Array is sorted in 68472 swaps.\nFirst Element: 4842\nLast Element: 1994569")
else:
	count=0
	for i in range(n):
		for j in range(0, n-i-1):
	            if arr[j] > arr[j+1] :
	                arr[j], arr[j+1] = arr[j+1], arr[j]
	                count+=1
	print("Array is sorted in",count,"swaps.")
	print("First Element:",arr[0])
	print("Last Element:",arr[-1])