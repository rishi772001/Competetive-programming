'''
@Author: rishi
'''


def find(arr, l, r):
    ans = r + 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == mid:
            l = mid + 1
        elif arr[mid] > mid:
            r = mid - 1
            ans = mid
    return ans


a = [0, 1, 2, 6, 9, 11, 15]
print(find(a, 0, len(a) - 1))
