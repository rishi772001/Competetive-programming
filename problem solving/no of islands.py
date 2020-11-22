#https://www.geeksforgeeks.org/find-number-of-islands/
def check(mat,r,c):
    if (r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0])):
        return 0
    else:
        return 1


def changeConnectedCells(mat,r,c):
    for i in range(r-1,r+2):
        for j in range(c - 1, c + 2):
            if(check(mat,i,j) and mat[i][j] == 1 ):
                mat[i][j] = 0
                changeConnectedCells(mat,i,j)



mat= [[1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [1, 0, 0, 1, 1],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 0, 1]]


count = 0
rows = len(mat)
cols = len(mat[0])
for i in range(rows):
    for j in range(cols):
        if(mat[i][j] == 1):
            count += 1
            mat[i][j] = 0
            changeConnectedCells(mat,i,j)

print(count)