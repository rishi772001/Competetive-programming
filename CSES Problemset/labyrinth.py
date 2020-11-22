'''
@Author: rishi
https://cses.fi/problemset/task/1193
'''
a = [
    [1,1,1,1,1,1,1,1],
    [1,0,'A',1,0,0,0,1],
    [1,0,1,1,0,1,'B',1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

def find(a, i, j, rows, cols, dist = 0, s = ""):
    if i < 0 or j < 0 or i > rows or j > cols or a[i][j] == 1:
        return False

    if a[i][j] == 'B':
        return [dist, s]
    a[i][j] = 1
    one = find(a, i + 1, j, rows, cols, dist + 1, s + 'D')
    two = find(a, i - 1, j, rows, cols, dist + 1, s + 'T')
    three = find(a, i, j + 1, rows, cols, dist + 1, s + 'R')
    four = find(a, i, j - 1, rows, cols, dist + 1, s + 'L')

    m = [2**32, None]
    if one and one[0] < m[0]:
        m = [one[0], one[1]]
    if two and two[0] < m[0]:
        m = [two[0], two[1]]
    if three and three[0] < m[0]:
        m = [three[0], three[1]]
    if four and four[0] < m[0]:
        m = [four[0], four[1]]
    return m

p,q = -1,-1
row_length = len(a)
col_length = len(a[0])
flag = False
for i in range(row_length):
    for j in range(col_length):
        if a[i][j] == 'A':
            p,q = i,j
            flag = True
            break
    if flag:
        break


ans = find(a, p, q, row_length, col_length)
if not ans or ans[1] == None:
    print("NO")
else:
    print(ans[0])
    print(ans[1])
