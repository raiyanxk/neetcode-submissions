class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        l = 0
        r = len(height) - 1

        maxL = 0
        maxR = 0

        while l <= r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)

            if maxL < maxR:
                res += max(0, min(maxL, maxR) - height[l])
                l += 1
            else:
                res += max(0, min(maxL, maxR) - height[r])
                r -= 1
            
        return res 
        