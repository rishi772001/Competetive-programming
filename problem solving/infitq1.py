'''
@Author: rishi
'''
import sys


def function(arr):
    size = len(arr)
    ans = [0] * size

    for i in range(size):
        temp = {}
        for j in range(i + 1, size):
            if arr[j] > arr[i]:
                if arr[j] in temp:
                    temp[arr[j]] += 1
                else:
                    temp[arr[j]] = 1
        if len(temp) <= 0:
            ans[i] = -1
        else:
            val = max(temp.values())
            mini = sys.maxsize
            for k in temp:
                if temp[k] == val and k < mini:
                    mini = k
            ans[i] = mini
    return ans


arr = list(map(int, input().split(",")))
out = ""
for i in function(arr):
    out += str(i)
    out += ","
print(out[:-1])
