# https://leetcode.com/problems/summary-ranges/

arr = [0,2,3,4,6,8,9]

out = []
i = 0
while i < len(arr):
    start = arr[i]
    st = ""
    st += str(arr[i])
    while i < len(arr)-1 and arr[i]+1 == arr[i+1]:
        i += 1
    if arr[i] != start:
        st += "->"+str(arr[i])
    out.append(st)
    i += 1
print(out)