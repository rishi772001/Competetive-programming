'''
@Author: rishi
https://www.techiedelight.com/find-substrings-string-permutation-given-string/
'''

x = "XYYZXZYZXXYZ"
y = set("XYZ")

n = len(y)

window = []
for i in range(n):
    window.append(x[i])
if sorted(window) == sorted(y):
    print(x[0:n])

for i in range(n, len(x)):
    window.remove(x[i - n])
    window.append(x[i])
    if sorted(window) == sorted(y):
        print(x[i - n:i])
