'''
@Author: rishi
https://leetcode.com/problems/valid-sudoku/
'''

from collections import defaultdict


def isValidSudoku(board):
    rowdict = defaultdict(list)
    coldict = defaultdict(list)
    boxdict = defaultdict(list)

    for row in range(9):
        for col in range(9):
            if board[row][col] != ".":
                val = board[row][col]
                if val in rowdict[row]:
                    return False
                rowdict[row].append(val)

                if val in coldict[col]:
                    return False
                coldict[col].append(val)

                box_index = (row // 3) * 3 + col // 3
                if val in boxdict[box_index]:
                    return False
                boxdict[box_index].append(val)
    return True


board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValidSudoku(board))
