from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if (sum(nums) - S) % 2 == 1:
            return 0
        B = (sum(nums) - S) // 2
        dp = [0] * (B+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(B, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]

s = Solution()
nums = [1,1,1,1,1]
res = s.findTargetSumWays(nums, 3)
print(res)