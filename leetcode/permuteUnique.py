from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        start = 0
        nums = sorted(nums)
        visited = [0]*len(nums)

        def backtrack(temp, visited):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                    continue
                elif visited[i] == 0:
                    visited[i] = 1
                    temp.append(nums[i])
                    backtrack(temp, visited)
                    temp.pop()
                    visited[i] = 0
        backtrack(temp, visited)

        return res


s = Solution()
nums = [1,1,2, 3]
res = s.permuteUnique(nums)
print(res)