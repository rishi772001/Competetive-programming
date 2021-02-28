'''
@Author: rishi
'''


# function to find pivot index => both left and right is smaller
def find_pivot(arr, l, r):
    if (arr[r] > arr[l]):
        return 0
    if l == r:
        return l

    while l <= r:
        mid = l + (r - l) // 2
        if mid < r and arr[mid + 1] < arr[mid]:
            return mid

        if mid > l and arr[mid] < arr[mid - 1]:
            return mid - 1

        if arr[l] > arr[mid]:
            r = mid - 1
        else:
            l = mid + 1


def binary_search(arr, l, r, val):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def find_no_of_rotations(arr, pivot):
    return pivot + 1


a = [5, 8, 3]
val = 5
pivot = find_pivot(a, 0, len(a) - 1)
print(pivot)
if a[0] <= val <= a[pivot]:
    print(binary_search(a, 0, pivot, val))
else:
    print(binary_search(a, pivot + 1, len(a) - 1, val))

print("no of rotations = ", find_no_of_rotations(a, pivot))
