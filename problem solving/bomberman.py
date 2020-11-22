import os
import sys


def putBomb(grid, r, c):
    for i in range(r):
        for j in range(c):
            if (grid[i][j] == '.'):
                grid[i][j] = '3'


def decrement(grid, r, c):
    for i in range(r):
        for j in range(c):
            if (grid[i][j] != '.'):
                grid[i][j] = str(int(grid[i][j]) - 1)


def explode(grid, r, c):
    for i in range(r):
        for j in range(c):
            if (grid[i][j] == '0'):
                if (i - 1 >= 0 and grid[i - 1][j] != grid[i][j]):
                    grid[i - 1][j] = '.'
                if (i + 1 < r and grid[i + 1][j] != grid[i][j]):
                    grid[i + 1][j] = '.'
                if (j - 1 >= 0 and grid[i][j - 1] != grid[i][j]):
                    grid[i][j - 1] = '.'
                if (j + 1 < c and grid[i][j + 1] != grid[i][j]):
                    grid[i][j + 1] = '.'
                grid[i][j] = '.'


def bomberMan(n, grid, r, c):
    if (n == 1):
        return grid
    n = n % 4 + 4
    decrement(grid, r, c)
    for sec in range(2, n + 1):
        if (sec % 2 == 0):
            decrement(grid, r, c)
            putBomb(grid, r, c)
        elif (sec % 2 != 0):
            decrement(grid, r, c)
            explode(grid, r, c)
    return grid


if __name__ == '__main__':

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid_item = grid_item.replace('O', '3')

        grid.append(list(grid_item))

    result = bomberMan(n, grid, r, c)
    for i in range(r):
        for j in range(c):
            if (result[i][j] != '.'):
                print("O", end="")
            else:
                print(".", end="")
        print()

    # fptr.write('\n'.join(result))

