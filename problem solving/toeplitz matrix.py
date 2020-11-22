'''
@Author: rishi
https://leetcode.com/problems/toeplitz-matrix/
print all diagonals in matrix
'''


def isToeplitzMatrix(a):
    # starting from top row

    for i in range(len(a[0])):
        index_1 = 0
        index_2 = i
        val = a[index_1][index_2]
        while index_1 < len(a) and index_2 < len(a[0]):

            if a[index_1][index_2] != val:
                return False
            index_1 += 1
            index_2 += 1

    # starting from left col

    for i in range(1, len(a)):
        index_1 = i
        index_2 = 0
        val = a[index_1][index_2]

        while index_1 < len(a) and index_2 < len(a[0]):
            if a[index_1][index_2] != val:
                return False
            index_1 += 1
            index_2 += 1
    return True


matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

print(isToeplitzMatrix(matrix))