from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(0, j+1):
                if i == j: dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return True if dp[0][n-1] > 0 else False