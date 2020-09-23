
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        elif n==3: return 2
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        for i in range(4, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], dp[j]*dp[i-j])
        return dp[n] % 1000000007

    def cuttingRope1(self, n: int) -> int:

        lenMap = {1:0, 2:1}
        def dfs(n):
            if n in lenMap:
                return lenMap[n]
            lenMap[n] = -1
            for i in range(1, n//2+1):
                lenMap[n] = max(lenMap[n], i*(n-i), i*dfs(n-i))
            return lenMap[n]
        return lenMap(n)






s = Solution()
res = s.cuttingRope(4)
print(res)