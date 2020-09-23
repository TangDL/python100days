from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        dp = [0, 0]
        dp[1] = -prices[0]
        for i in range(1, n):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[0] - prices[i])
        return dp[0]