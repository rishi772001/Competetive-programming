'''
@Author: rishi
'''

arr = [1, 2, 3, 4, 5, 6]
out = arr.copy()
# to find sum of all elements from starting to current
# normal method(O(n*n))
for i in range(len(arr)):
    sum = 0
    for j in range(i):
        sum += arr[j]
    out[i] = sum + arr[i]
print(out)
# prefix sum algorithm(O(n))
for i in range(1, len(arr)):
    out[i] = arr[i] + out[i - 1]
print(out)
