'''
@Author: rishi
https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
'''

# key idea -> prefix sum becomes 0 or repeat again if such sub array exist
arr = [-3, 2, 3, 1, 6]


def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]


prefix_sum(arr)
sums = set()
for i in arr:
    if i == 0 or i in sums:
        print("True")
        exit(0)
    sums.add(i)
print("False")
