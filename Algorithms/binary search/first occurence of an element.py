'''
@Author: rishi
'''


def binary_search(arr, l, r, val, first=True):
    ans = -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == val:
            ans = mid
            # for first value search to the left of curr
            if first:
                r = mid - 1
            # for last value search to the right of curr
            else:
                l = mid + 1
        elif arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return ans


arr = [2, 5, 5, 5, 5, 6, 8, 9, 9, 9]
val = 5

first = binary_search(arr, 0, len(arr), val)
last = binary_search(arr, 0, len(arr), val, first=False)
print("first occurrence = ", first)
print("last occurrence = ", last)
print("occurrences = ", last - first + 1)
