'''
@Author: rishi
'''


def quicksort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quicksort(arr, pivot + 1, r)
        quicksort(arr, l, pivot - 1)


def partition(arr, l, r):
    p = l  # pivot element
    i = l + 1
    j = r

    while i < j:
        while arr[i] < arr[p]:
            i += 1
        while arr[j] > arr[p]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[p] = arr[p], arr[j]
    return j


arr = [8, 1, 6, 2, 3, 7, 6, 4, 19, 5, 4, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)
