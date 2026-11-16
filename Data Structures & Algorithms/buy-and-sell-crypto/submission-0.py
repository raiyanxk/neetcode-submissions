class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = float('inf')
        res = 0

        for price in prices:
            res = max(res, price - low)
            low = min(price, low)
        
        return res