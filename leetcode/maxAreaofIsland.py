from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j, temp):
            if grid[i][j] == 1:
                temp += 1
                grid[i][j] = 2
                if i > 0: temp = dfs(i-1, j, temp)
                if j > 0: temp = dfs(i, j-1, temp)
                if i < n-1: temp = dfs(i+1, j, temp)
                if j < m-1: temp = dfs(i, j+1, temp)
            return temp
        res = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    temp = dfs(i, j, 0)
                    if temp > res: res = temp
        return res