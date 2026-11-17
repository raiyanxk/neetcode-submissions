class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        small = float('inf')

        for p in prices:
            res = max(p - small, res)
            small = min(small, p)
        
        return res 