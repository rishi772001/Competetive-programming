'''
@Author: rishi

# linear time sorting algorithm
# used since counting sort cannot store integers
uses insertion sort as sub routine
'''


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j - 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    # create buckets for uniformly distributed values
    buckets = [[] for _ in range(10)]
    # calculate and add each every element to correct bucket
    for i in arr:
        bucket_index = int(i * 10)
        buckets[bucket_index].append(i)
    # sort all buckets
    for i in buckets:
        insertion_sort(i)
    # copy values back from buckets to array
    k = 0
    for i in buckets:
        for j in i:
            arr[k] = j
            k += 1


a = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(a)
print(a)
