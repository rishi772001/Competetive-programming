'''
@Author: rishi
'''


# max heap heapify function
# takes heap represented as array as parameter

# assuming that only the ith node is not in the part of heap
def heapify(arr, i=0):
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child < len(arr) and arr[left_child] > arr[i]:
        largest = left_child
    else:
        largest = i

    if right_child < len(arr) and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        # swap
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest)


# the array to be converted to heap
array = [1, 5, 3, 2, 4, 15, 8]

# start from the last internal node because for the function heapify
# we assume that the sub tree to be a heap
# initially only the leaf nodes are guaranteed to be heap
start_idx = (len(array) // 2) - 1

for i in range(start_idx, -1, -1):
    heapify(array, i)
print(array)
