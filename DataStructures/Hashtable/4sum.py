'''
@Author: rishi
'''


def four_sum(s, arr):
    # store all sums and their combinations in map
    sums = {}
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            sums[arr[i] + arr[j]] = [i, j]

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            temp = arr[i] + arr[j]
            to_find = s - temp
            if to_find in sums:
                return i, j, sums[to_find][0], sums[to_find][1]
