arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = []
even = []
result = []
for i in arr:
    if arr.index(i) % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
odd.sort()
even.sort(reverse=True)
print(odd)
print(even)
for i in range(max(len(odd), len(even))):
    if i < len(even):
        result.append(even[i])
    if i < len(odd):
        result.append(odd[i])

print(result)
