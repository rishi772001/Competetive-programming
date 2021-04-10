def permute(arr, l, r):  # n!
    if l == r:
        print(arr)
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        permute(arr, l + 1, r)
        arr[l], arr[i] = arr[i], arr[l]


a = [1, 2, 3, 4]
print(permute(a, 0, 3))


def combination(arr, remain, comb, nex):
    """
    :param arr: array for which to find combination
    :param remain: combination size
    :param comb: array to store combination values
    :param nex: nex variable for iteration
    """
    if remain == 0:
        print(comb)
    else:
        for i in range(nex, len(arr) + 1):
            comb.append(arr[i])
            combination(arr, remain - 1, comb, i + 1)
            comb.pop()


arr = [1, 2, 3]
# permute(arr, 0, 2)
print("-------------")
# combination(arr, 2, [], 1)
