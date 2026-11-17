class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def compute(rate, arr):
            res = 0

            for num in arr:
                res += (num + rate - 1) // rate

            return res

        
        slow = 1
        fast = max(piles)
        best = fast

        while slow <= fast:

            mid = (slow + fast) // 2
            time = compute(mid, piles)

            if time <= h:
                fast = mid - 1
                best = mid
            else:
                slow = mid + 1

        return best