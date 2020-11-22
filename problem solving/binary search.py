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


a = [5,7,7,8,8,10]
print(binarysearch(a,0,len(a)-1,6))