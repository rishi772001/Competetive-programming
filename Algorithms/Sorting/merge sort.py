def merge(b,c,a):
    p = len(b)
    q = len(c)
    i = j = k = 0

    # i => traverse b array
    # j => traverse c array
    # k => traverse a array  => Merged array

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


def mergesort(a):
    n = len(a)
    if n > 1:
        b = a[:(n // 2)]
        c = a[(n // 2):]
        mergesort(b)
        mergesort(c)
        merge(b,c,a)


#arr = [64, 34, 25, 12, 22, 11, 90]
arr = [3, 2, 4, 1, 5, 70]
mergesort(arr)
print(arr)