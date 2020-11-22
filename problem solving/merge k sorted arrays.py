
def merge2array(b, c, a = None):
    p = len(b)
    q = len(c)
    if(a is None):
        a = [0 for i in range(p+q)]

    i = j = k = 0
    while i < p and j < q:
        if(b[i] <= c[j]):
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    if(p == i):     # Add remaining elements from c to a array
        while j < q:
            a[k] = c[j]
            j += 1
            k += 1
    else:           # Add remaining elements from b to a array
        while i < p:
            a[k] = b[i]
            i += 1
            k += 1
    return a


def mergeksortedarray(arr,k):
    if k == 1:
        return arr[0]
    elif k == 2:
        return merge2array(arr[0],arr[1])
    else:
        a = arr[:k//2]
        b = arr[k//2:]
        a = mergeksortedarray(a, k // 2)
        if(k % 2 != 0):
            b = mergeksortedarray(b, k // 2 + 1)
        else:
            b = mergeksortedarray(b, k // 2)
        out = merge2array(a, b)
        return out

arr = [[2, 6, 12, 34],
       [1, 9, 20, 1000],
       [23, 34, 90, 2000],
       [50,100,150]]

k = 4
print(mergeksortedarray(arr,k))