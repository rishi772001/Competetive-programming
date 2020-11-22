def find_neighbour(a, row, col, rows, cols): #return an array of neighbouring cells
    if rows == 1 and cols == 1:
        return []
    if rows == 1:
        if col - 1 < 0:
            return [a[row][col + 1]]
        elif col + 1 >= cols:
            return [a[row][col - 1]]
        else:
            return [a[row][col - 1], a[row][col + 1]]
    if cols == 1:
        if row - 1 < 0:
            return [a[row + 1][col]]
        elif row + 1 >= rows:
            return [a[row - 1][col]]
        else:
            return [a[row + 1][col], a[row - 1][col]]
    if row - 1 < 0:
        if col - 1 < 0:
            neighbour = [a[row + 1][col],
                        a[row][col + 1],
                        a[row + 1][col + 1]]

        elif col + 1 >= cols:
            neighbour = [a[row][col - 1],
                         a[row + 1][col],
                         a[row + 1][col - 1]]
        else:
            neighbour = [a[row][col - 1],
                        a[row + 1][col],
                        a[row][col + 1],
                        a[row + 1][col + 1],
                        a[row + 1][col - 1]]

    elif row + 1 >= rows:
        if col - 1 < 0:
            neighbour = [a[row - 1][col],
                        a[row][col + 1],
                        a[row - 1][col + 1]]
        elif col + 1 >= cols:
            neighbour = [
                a[row - 1][col],
                a[row][col - 1],
                a[row - 1][col - 1],
            ]
        else:
            neighbour = [
                a[row - 1][col],
                a[row][col - 1],
                a[row][col + 1],
                a[row - 1][col - 1],
                a[row - 1][col + 1],
            ]
    else:
        if col - 1 < 0:
            neighbour = [a[row - 1][col],  # top
                         a[row][col + 1],  # right
                         a[row + 1][col],  # bottom
                         a[row - 1][col + 1],  # topri8
                         a[row + 1][col + 1],  # bottomright
                         ]
        elif col + 1 >= cols:
            neighbour = [a[row - 1][col],  # top
                         a[row][col - 1],  # left
                         a[row + 1][col],  # bottom
                         a[row - 1][col - 1],  # topleft
                         a[row + 1][col - 1],  # bottomleft
                         ]
        else:
            neighbour = [a[row - 1][col],  #top
                         a[row][col - 1],  #left
                         a[row][col + 1],  #right
                         a[row + 1][col],  #bottom
                         a[row - 1][col - 1],  # topleft
                         a[row - 1][col + 1],  # topri8
                         a[row + 1][col + 1],  # bottomright
                         a[row + 1][col - 1],  # bottomleft
                         ]
    return neighbour

# a = [[1,2,3,4,5,6,7,8,9,10]]
# print(find_neighbour(a, 0, 3, 1, 10))