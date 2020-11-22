mat = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36]
]


r = 2 # no of rotations

rows = len(mat)
cols = len(mat[0])

for i in range(min(rows,cols) // 2):
    temp = list()
    for a in range(i, cols - i):
        temp.append(mat[i][a])

    for b in range(i+1, rows - i):
        temp.append(mat[b][cols - 1 - i])

    for c in range(cols - 2 - i, i-1, -1):
        temp.append(mat[rows-1-i][c])

    for d in range(rows - 2 - i, i, -1):
        temp.append(mat[d][i])

    n = len(temp)
    k = r%n
    # temp = temp[n-k:]+temp[:n-k]  # Clockwise

    temp = temp[k:]+temp[:k]    # Anticlockwise

    for a in range(i, cols - i):
        mat[i][a] = temp.pop(0)

    for b in range(i+1, rows - i):
        mat[b][cols - 1 - i] = temp.pop(0)

    for c in range(cols - 2 - i, i-1, -1):
        mat[rows-1-i][c] = temp.pop(0)

    for d in range(rows - 2 - i, i, -1):
        mat[d][i] = temp.pop(0)

for i in mat:
    print(i)