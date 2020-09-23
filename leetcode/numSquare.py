from typing import List
import numpy as np

class Solution:
    def numSquares(self, n: int) -> int:
        nums = int(np.floor(np.sqrt(n)) +1)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, nums):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j-i*i] +1)
        return dp[-1]


s = Solution()
res = s.numSquares(1)
print(res)