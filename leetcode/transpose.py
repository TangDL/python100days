from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:

        c, r = len(A[0]), len(A)
        if r == 0:
            return []
        B = [[0]*r for _ in range(c)]

        for i in range(c):
            for j in range(r):
                B[i][j] = A[j][i]
        return B

s = Solution()
res = s.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(res)