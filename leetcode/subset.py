from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, temp):
            if len(temp) <= len(nums):
                res.append(temp[:])

            for i in range(start, len(nums)):
                temp.append(nums[i])
                dfs(start+1, temp)
                temp.pop()

        dfs(0, [])
        return res