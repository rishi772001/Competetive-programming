from itertools import permutations
n=9
ar=[]

for i in range(1, n + 1):
    if n % i == 0:
        ar.append(i)
print(ar)
for i in permutations(ar):
    print(i)
