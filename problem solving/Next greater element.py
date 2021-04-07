'''
@Author: rishi

Amazon interview question

Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element
on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1.

a = [4,5,2,1,25]
output = [5,25,25,25,-1]
'''

a = [11, 13, 21, 3]


# efficient method
def next(a):
    # stack
    s = [a[0]]
    i = 1
    ans = {}
    while i < len(a):
        val = s[-1]
        if a[i] > val:
            ans[s.pop()] = a[i]
        s.append(a[i])
        i += 1
    while s:
        ans[s.pop()] = -1
    print(ans)


print(next(a))
# Bruteforce method(O(N*N))
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[j] > a[i]:
            a[i] = a[j]
            break
    else:
        a[i] = -1


print(a)
