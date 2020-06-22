# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

arr = [50, 3, 10, 7, 40, 80]
ans = []

for i in range(len(arr)):
    c = 0
    for j in range(i,len(arr)-1):
        if(arr[j] < arr[j+1]):
            c += 1
    ans.append(c)
print(max(ans)+1)
