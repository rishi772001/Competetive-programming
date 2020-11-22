from neighbourcells import find_neighbour

a = [[1,2,3,4,5,6,7,8,9,10]]

b = [[0]*len(a[0]) for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(a[0])):
        n = find_neighbour(a, i, j,len(a), len(a[0]))
        print(n)
        s = a[i][j] + sum(n)
        b[i][j] =  s // (len(n) + 1)

print(b)

