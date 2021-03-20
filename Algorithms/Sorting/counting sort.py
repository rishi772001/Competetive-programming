'''
@Author: rishi

# o(n) -> linear time sorting algorithm
# used when range is less and elements is more
# not a comparison based sorting
'''


def counting_sort(arr):
    count = [0] * 10
    size = len(arr)
    output = [0] * size
    # Store the count of each elements in count array
    for i in range(0, len(arr)):
        count[arr[i]] += 1

    # Store the cumulative count
    # this stores the starting index of the element
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        # reduce the starting index
        i -= 1

    return output


arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
