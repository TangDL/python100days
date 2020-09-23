from typing import List

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        if max(A) == min(A): return 1
        dp = [1] * (n+1)
        for i in range(1, n-1):
            if A[i-1] > A[i] < A[i+1] or A[i-1] < A[i] > A[i+1]:
                dp[i] = dp[i-1] + 1
        return max(dp) + 1



s =Solution()
A = [9,4,2,10,7,8,8,1,9]
res = s.maxTurbulenceSize(A)
print(res)