from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(visited, i, j, res):
            if i == m-1 and j == n-1:
                return res+1
            if i<0 or j < 0 or i > m-1 or j > n-1 or visited[i][j]:
                return res
            for dir in ((1, 0), (0, 1)):
                visited[i][j] = True
                new_i, new_j = i+dir[0], j + dir[1]
                res = dfs(visited, new_i, new_j, res)
                visited[i][j] = False
            return res

        visited = [[False] * n for _ in range(m)]
        res = 0
        res = dfs(visited, 0, 0, res)

        return res

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
