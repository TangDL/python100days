from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        res = float('inf')
        def dfs(cur, cost, k):
            nonlocal res
            if cur == dst:
                res = min(res, cost)
                return
            if cur > res or k < 0:
                return
            for i in range(len(flights)):
                if flights[i][0] == cur:
                    dfs(flights[i][1], cost+flights[i][2], k-1)

        dfs(src, 0, K)
        return res if res!=float('inf') else -1

    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        res = float('inf')
        visited = [0] * n
        visited[src] = 1

        def dfs(cur, cost, k, visited):
            nonlocal res
            if cur == dst:
                res = min(res, cost)
                return
            if cur > res or k < 0:
                return
            for i in range(len(flights)):
                if flights[i][0] == cur and visited[flights[i][1]] == 0:
                    visited[flights[i][1]] = 1
                    dfs(flights[i][1], cost + flights[i][2], k - 1, visited)
                    visited[flights[i][1]] = 0

        dfs(src, 0, K, visited)
        return res if res != float('inf') else -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf')] * n for _ in range(K+1)]
        for s, d, c in flights:
            if s == src:
                dp[0][d] = c

        for i in range(1, K+1):
            for s, d, c  in flights:
                dp[i][d] = min(dp[i-1][d], dp[i-1][s] + c, dp[i][d])
        return dp[-1][dst] if dp[-1][dst]!= float('inf') else -1

s = Solution()
edges = [[0,1,100],[1,2,100],[0,2,500]]
res = s.findCheapestPrice2(3, edges, 0, 2, 1)
print(res)