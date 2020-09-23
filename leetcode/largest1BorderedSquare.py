class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        l = [[[0]*n]*m]
        t = [[[0] * n] * m]

        maxlen = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l[i][j], t[i][j] = 1, 1
                if i>0: t[i][j] += t[i-1][j]
                if j>0: l[i][j] += l[i][j-1]
                for k in range(min(t[i][j], l[i][j]), 0, -1):
                    if k > maxlen and l[i+k+1][j] >= k and t[i][j-k+1] >= k:
                        maxlen = k
                        break
        return maxlen*maxlen