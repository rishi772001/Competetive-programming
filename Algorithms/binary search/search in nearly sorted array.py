'''
@Author: rishi
'''


def binary_search(arr, l, r, val):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == val:
            return mid
        elif mid + 1 <= r and arr[mid + 1] == val:
            return mid + 1
        elif mid - 1 >= l and arr[mid - 1] == val:
            return mid - 1

        elif arr[mid] > val:
            r = mid - 2
        else:
            l = mid + 2
    return -1


arr = [2, 1, 3, 5, 4, 7, 6, 8, 9]
print(binary_search(arr, 0, len(arr) - 1, 10))
