class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def calc(speed):
            res = 0

            for pile in piles:
                res += (pile + speed - 1) // speed

            return res 
        

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            time = calc(mid)

            if time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res