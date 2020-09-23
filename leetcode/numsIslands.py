from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i >= 1: dfs(i - 1, j)
                if j >= 1: dfs(i, j - 1)
                if i < row - 1: dfs(i + 1, j)
                if j < column - 1: dfs(i, j + 1)
            else: return

        res = 0
        if len(grid) == 0:
            return 0
        row, column = len(grid), len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res