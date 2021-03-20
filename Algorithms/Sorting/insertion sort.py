'''
@Author: rishi

O(n**2)
worst case : reversed array
'''


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # iterates from i - 1 to element less than key and moves one step for each
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # place the element in correct position
        arr[j + 1] = key


arr = [2, 4, 2, 8, 3, 3, 1]
insertion_sort(arr)
print(arr)
