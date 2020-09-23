from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return abs(sum(stones) - 2*dp[-1])


s = Solution()
stones = [2,7,4,1,8,1]
res = s.lastStoneWeightII(stones)
print(res)