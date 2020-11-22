global n, queens_placed
n = 4       # SIZE OF BOARD
board = [[0]*n for _ in range(n)]
queens_placed = {}

def queen(board, row, col):
    if len(queens_placed) == n:
        return True
    if col >= n or row >= n:
        return False
    # Find safe col in that row
    for i in range(col, n):
        flag = True
        for j in queens_placed:
            if(queens_placed[j][0] == row or queens_placed[j][1] == i          #SAME ROW OR COL
                or queens_placed[j][0] - queens_placed[j][1] == row - i         #SAME DIAGONAL1
                or queens_placed[j][0] + queens_placed[j][1] == row + i):       #SAME DIAGONAL2

                flag = False    # QUEEN CANNOT BE PLACED AT THIS CELL [ROW][I]
                break
        if flag:        # PLACE QUEEN AT [ROW][I]
            col = i
            break
    else:
        return False    # RETURN FALSE IF NO CELL FOUND

    board[row][col] = 1
    queens_placed[row] = [row, col]     # ADD POSITION
    if queen(board, row + 1, 0):
        return True                     # ADD NEXT QUEEN
    else:           # BACKTRACK
        board[row][i] = 0               # DELETE QUEEN
        del queens_placed[row]
        return queen(board, row, col + 1)





if queen(board, 0, 0):
    print("Successfully placed")
    print("Board after queens placed")
    for i in board:
        print(i)
    print("Positions")
    for i in queens_placed:
        print(queens_placed[i])
else:
    print("Could not place all queens")
