from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j, visited):
            if grid[i][j] == 0 or visited[i][j]:
                return 0
            ans = 1
            visited[i][j] = True
            if i > 0:
                ans += dfs(i-1, j, visited)
            if j > 0:
                ans += dfs(i, j-1, visited)
            if i < n-1:
                ans += dfs(i+1, j, visited)
            if j < m-1:
                ans += dfs(i, j+1, visited)
            return ans

        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited = [[False] * m for _ in range(n)]
                    grid[i][j] = 1
                    res_temp = dfs(i, j, visited)
                    res = max(res, res_temp)
                    grid[i][j] = 0
        return res if res else m*n
