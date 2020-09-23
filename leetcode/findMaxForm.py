from typing import List
from collections import defaultdict

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m+1) for _ in range(n+1)]
        for s in strs:
            cnt_0 = s.count('0')
            cnt_1 = s.count('1')
            for i in range(n, cnt_1-1, -1):
                for j in range(m, cnt_0-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt_1][j-cnt_0]+1)

        return dp[-1][-1]



s = Solution()
Array = {"10", "0001", "111001", "1", "0"}
res = s.findMaxForm(Array, 5, 3)
print(res)