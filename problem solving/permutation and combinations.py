def permute(arr, l, r):      # n!
    if l == r:
        print(arr)
    for i in range(l,r+1):
        arr[l], arr[i] = arr[i], arr[l]
        permute(arr, l+1, r)
        arr[l], arr[i] = arr[i], arr[l]


def combination(arr):
    pass


arr = [1, 2, 3]
permute(arr,0,2)
combination(arr)