'''
@Author: rishi
https://cses.fi/problemset/task/1192
'''
a = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,1],
    [1,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

def change(a,i,j, rows, cols):
    if i < 0 or j < 0 or i > rows or j > cols or a[i][j] == 1:
        return
    a[i][j] = 1
    change(a, i+1, j, rows, cols)
    change(a, i - 1, j, rows, cols)
    change(a, i, j+1, rows, cols)
    change(a, i, j-1, rows, cols)

row_length = len(a)
col_length = len(a[0])
count = 0
for i in range(row_length):
    for j in range(col_length):
        if a[i][j] == 0:
            count += 1
            change(a, i, j, row_length, col_length)
print(count)