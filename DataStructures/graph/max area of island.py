'''
@Author: rishi
https://leetcode.com/problems/max-area-of-island/submissions/
'''


class Solution:
    def __init__(self):
        self.max_area = 0

    def find_max(self, grid, row, col, tot_rows, tot_cols, curr_area=0):
        if row < 0 or row >= tot_rows:
            return curr_area
        if col < 0 or col >= tot_cols:
            return curr_area

        if grid[row][col] == 1:
            curr_area += 1

            grid[row][col] = 0

            curr_area = self.find_max(grid, row + 1, col, tot_rows, tot_cols, curr_area)
            curr_area = self.find_max(grid, row, col + 1, tot_rows, tot_cols, curr_area)
            curr_area = self.find_max(grid, row - 1, col, tot_rows, tot_cols, curr_area)
            curr_area = self.find_max(grid, row, col - 1, tot_rows, tot_cols, curr_area)

        return curr_area

    def maxAreaOfIsland(self, grid):
        tot_rows = len(grid)
        tot_cols = len(grid[0])
        for i in range(tot_rows):
            for j in range(tot_cols):
                if grid[i][j] == 1:
                    calc_area = self.find_max(grid, i, j, tot_rows, tot_cols)
                    if calc_area > self.max_area:
                        self.max_area = calc_area
        return self.max_area

s = Solution()
grid = [[0,0,0,0,0,1,1],
        [0,0,0,0,0,1,1],
        [1,1,1,1,0,0,0],
        [1,1,1,1,0,0,0],
        [1,1,1,1,0,0,0],
        [1,1,1,1,0,0,0]]

print(s.maxAreaOfIsland(grid))