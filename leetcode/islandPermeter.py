from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        gridperimeter = 4
        n = len(grid)
        if n==0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += gridperimeter
                if i>1 and grid[i-1][j] == 1:
                    res -= 1
                if j > 1 and grid[i][j-1] == 1:
                    res -= 1
                if i < n-1 and grid[i+1][j] == 1:
                    res -= 1
                if j < m-1 and grid[i][j+1] == 1:
                    res -= 1
        return res