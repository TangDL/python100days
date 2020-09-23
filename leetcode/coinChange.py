from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        temp = amount // min(coins) + 1
        dp = [temp] * (amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        return dp[-1]