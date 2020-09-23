class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            mins = n
            for j in range(1, i):
                if i%j == 0:
                    dp[i] = min(dp[j] + i//j, mins)
                    mins = dp[i]
        return dp[n]



# s = Solution()
# res = s.minSteps(3)
# print(res)

print(str(chr(ord('a')+1)))