from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0: return 0
        lowest = prices[0]
        res = 0
        for i in range(1, n):
            if prices[i] < lowest: lowest = prices[i]
            else: res = max(prices[i] - lowest, res)
        return res
