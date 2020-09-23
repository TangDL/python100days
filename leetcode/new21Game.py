class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [float('-inf')] * (K+W)
        s = 0
        for i in range(K, K+W):
            dp[i] = 1 if i<= N else 0
            s += dp[i]
        for i in range(K-1, -1, -1):
            dp[i] = 1/W * s
            s = s + dp[i] - dp[i+W]
        return dp[0]


s = Solution()
res = s.new21Game(21, 17, 10)
print(res)
