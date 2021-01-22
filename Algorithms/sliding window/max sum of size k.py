'''
@Author: rishi
'''

arr = [1, 2, 3, 4, 5]
k = 3

if k > len(arr):
    print(sum(arr))
    exit(0)

window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    curr_sum = window_sum + arr[i] - arr[i - k]
    window_sum = max(curr_sum, window_sum)
print(window_sum)
