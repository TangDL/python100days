from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        time = k
        n = len(arr)
        cur = arr[0]
        if k >= n: return max(arr)

        for i in range(1, n):
            if cur > arr[i]:
                time -= 1
            else:
                cur = arr[i]
                time = k-1
            if time==0:break
        return cur


s = Solution()
arr = [1,11,22,33,44,55,66,77,88,99]
res = s.getWinner(arr, 9999999)
print(res)