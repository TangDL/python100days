from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def dfs(i, j, walks):

            if i<0 or j<0 or i>n-1 or j>m-1 or grid[i][j]==-1:
                return 0
            if grid[i][j] == 2:
                return 1 if walks == 0 else 0
            if walks == 0:
                return 0
            res = 0
            grid[i][j] = -1
            for dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_i, new_j = i + dir[0], j + dir[1]
                res += dfs(new_i, new_j, walks-1)
            grid[i][j] = 0
            return res

        walks = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    walks += 1
        res = dfs(start[0], start[1], walks+1)
        return res

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
s = Solution()
res = s.uniquePathsIII(grid)
print(res)