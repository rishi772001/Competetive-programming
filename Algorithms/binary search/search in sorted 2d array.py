def binary(arr, key, l, r):
    if l < r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binary(arr, key, l, mid - 1)
        if arr[mid] < key:
            return binary(arr, key, mid + 1, r)
    elif l == r and arr[l] == key:
        return l
    else:
        return -1
def search(a, key):
    for i in range(len(a)):
        if key < a[i][-1]:
            return [i, binary(a[i], key, 0, len(a[i]))]
        elif key == a[i][-1]:
            return [i, len(a[i] - 1)]
    return -1


a = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]


key = 16

print(search(a, key))